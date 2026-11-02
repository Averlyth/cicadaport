#!/usr/bin/env python3
"""Isolated UDP S7 cell: only locally bound 127.0.0.1 and local rust-udp binary.

Works on Python 3.10-3.13, Ubuntu 22.04/24.04. No Git, pip, Cargo,
external network, public selector, or service detection. `--check` opens no socket.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import socket
import stat
import subprocess
import sys
import threading

HEAD='2cd2f5a03451ce91cfe34780e8c4cd63b0c08071'
CAP_FIELDS={'contract_version':2, 'protocol':'udp', 'allowed_target':'127.0.0.1',
            'address_scope':'ipv4_loopback_only','public_api':False,
            'operational_go':False,'g8_live':'NO_GO_OPERACIONAL',
            'distribution_identity':'NOT_VERIFIED'}
class Stop(Exception): pass
def need(cond,msg):
    if not cond:raise Stop(msg)
def sha(data):return hashlib.sha256(data).hexdigest()
def regular(p):
    p=Path(p)
    need(p.is_file() and not p.is_symlink() and stat.S_ISREG(p.stat().st_mode),'NOT_REGULAR_BINARY:'+str(p))
    need(os.access(p,os.X_OK),'BINARY_NOT_EXECUTABLE')
    need(p.read_bytes()[:4]==b'\x7fELF','BINARY_NOT_ELF')
    return p
def host_identity():
    data={}
    f=Path('/etc/os-release')
    if f.is_file():
        for line in f.read_text('utf-8').splitlines():
            if '=' in line:
                k,v=line.split('=',1);data[k]=v.strip('"')
    name=data.get('ID','unknown'); version=data.get('VERSION_ID','unknown')
    py='{}.{}'.format(sys.version_info.major,sys.version_info.minor)
    recognized=name=='ubuntu' and version in ('22.04','24.04') and py in ('3.10','3.11','3.12','3.13')
    return {'os':name,'os_version':version,'python':py,'arch':platform.machine(),
            'matrix_cell':name+'-'+version+'-py'+py,'is_matrix_cell':recognized}
def process(binary,args,payload=b'',timeout=15):
    env={k:v for k,v in os.environ.items() if k not in ('LD_PRELOAD','LD_LIBRARY_PATH','RUST_LOG','RUST_BACKTRACE')}
    env['CICADAPORT_UDP_PUBLIC']='0';env['RUSTUP_AUTO_INSTALL']='0'
    return subprocess.run([str(binary)]+list(args),input=payload,capture_output=True,
                          timeout=timeout,env=env,check=False)
def cap_check(binary):
    p=process(binary,['--udp-capabilities-json'])
    need(p.returncode==0 and not p.stderr and 0<len(p.stdout)<8192,'CAPABILITIES_PROCESS_FAILED')
    need(p.stdout.endswith(b'\n') and p.stdout.count(b'\n')==1,'CAPABILITIES_NOT_ONE_JSONL')
    cap=json.loads(p.stdout)
    need(type(cap) is dict,'CAPABILITIES_NOT_OBJECT')
    for k,v in CAP_FIELDS.items(): need(cap.get(k)==v,'CAPABILITIES_FIELD_DRIFT:'+k)
    need(cap.get('max_ports_per_request')==32 and cap.get('max_workers')==16 and
         cap.get('max_timeout_ms')==500 and cap.get('max_request_bytes')==8192,
         'CAPABILITIES_LIMIT_DRIFT')
    need(cap.get('repository_head')==HEAD,'CAPABILITIES_HEAD_DRIFT')
    return {'sha256':sha(p.stdout),'capabilities':cap}
def negative_tests(binary):
    cases=[('bad_json', ['--udp-request-stdin'],b'{bad-json'),
           ('ambiguous_flags',['--udp-request-stdin','--udp-capabilities-json'],b''),
           ('wrong_protocol',['--udp-request-stdin'],
            b'{"contract_version":2,"record_type":"udp_scan_request","protocol":"tcp","target":"127.0.0.1","ports":[9],"workers":1,"timeout_ms":100,"probe_profile":"loopback_echo_v1"}')]
    out=[]
    for label,argv,payload in cases:
        p=process(binary,argv,payload)
        need(p.returncode==1 and p.stdout==b'' and
             p.stderr.startswith(b'P0A5_UDP_ENGINE=STOP:'),'NEGATIVE_FAILED:'+label)
        out.append(label)
    return out
def echo_probe(binary):
    """At most one local datagram, only IPv4 loopback, 200ms Rust timeout."""
    state={'payload_received':False,'error':None}
    with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as server:
        server.bind(('127.0.0.1',0));server.settimeout(4.0)
        port=server.getsockname()[1]
        need(server.getsockname()[0]=='127.0.0.1','NOT_LOOPBACK_BOUND')
        def once():
            try:
                payload,addr=server.recvfrom(4096)
                need(addr[0]=='127.0.0.1','NON_LOOPBACK_PEER')
                need(0<len(payload)<=4096,'ECHO_INVALID_PAYLOAD')
                state['payload_received']=True
                server.sendto(payload,addr)
            except (OSError,Stop) as err:state['error']=str(err)
        thread=threading.Thread(target=once,daemon=True);thread.start()
        request={'contract_version':2,'record_type':'udp_scan_request',
                 'protocol':'udp','target':'127.0.0.1','ports':[port],
                 'workers':1,'timeout_ms':200,'probe_profile':'loopback_echo_v1'}
        data=(json.dumps(request,separators=(',',':'))+'\n').encode()
        need(len(data)<8192,'REQUEST_TOO_LONG')
        run=process(binary,['--udp-request-stdin'],data,timeout=12)
        thread.join(timeout=4.2)
        need(not thread.is_alive() and state['error'] is None,'ECHO_SERVER_FAILED:'+str(state['error']))
        need(state['payload_received'],'NO_LOOPBACK_PROBE_RECEIVED')
        need(run.returncode==0 and not run.stderr and 0<len(run.stdout)<32768,
             'RUST_ECHO_PROCESS_FAILED:RC='+str(run.returncode)+':'+run.stderr.decode('utf-8','replace')[:220])
        records=[json.loads(line) for line in run.stdout.splitlines() if line]
        need(records and all(type(record) is dict for record in records),'ECHO_OUTPUT_NOT_JSONL')
        # Do not infer open/closed semantics from UDP without a verified payload contract.
        # Record actual response for scientific review, never call it public service detection.
        return {'loopback_port':port,'datagram_received':True,'records':records,
                'stdout_sha256':sha(run.stdout),'record_count':len(records)}
def run(argv=None):
    ap=argparse.ArgumentParser()
    modes=ap.add_mutually_exclusive_group(required=True)
    modes.add_argument('--check',action='store_true')
    modes.add_argument('--run',action='store_true')
    ap.add_argument('--binary',required=True)
    ap.add_argument('--expected-sha256',required=True)
    ap.add_argument('--output')
    ap.add_argument('--require-matrix-cell',action='store_true')
    args=ap.parse_args(argv)
    need(len(args.expected_sha256)==64 and all(c in '0123456789abcdef' for c in args.expected_sha256),
         'EXPECTED_SHA_FORMAT')
    binary=regular(Path(args.binary))
    need(sha(binary.read_bytes())==args.expected_sha256,'BINARY_SHA256_MISMATCH')
    host=host_identity()
    need(sys.platform=='linux' and host['arch'] in ('x86_64','amd64'),'LINUX_X86_64_REQUIRED')
    need(host['python'] in ('3.10','3.11','3.12','3.13'),'UNSUPPORTED_PYTHON')
    if args.require_matrix_cell: need(host['is_matrix_cell'],'NOT_REAL_UBUNTU_PYTHON_MATRIX_CELL')
    caps=cap_check(binary)
    if args.check:
        need(not args.output,'CHECK_MUST_NOT_WRITE_REPORT')
        print('P0A5_S7_CELL=PASS_CHECK:'+host['matrix_cell']+':MATRIX='+str(host['is_matrix_cell']))
        return 0
    need(os.environ.get('P0A5_S7_CELL_ALLOW_LOOPBACK')=='1','LOOPBACK_EXPLICIT_AUTH_REQUIRED')
    need(args.output is not None,'OUTPUT_REQUIRED')
    output=Path(args.output)
    need(not output.exists() and not output.is_symlink() and output.parent.is_dir(),
         'OUTPUT_ALREADY_EXISTS_OR_PARENT_MISSING')
    # Caller must ensure new evidence directory is outside all Git worktrees.
    negative=negative_tests(binary)
    positive=echo_probe(binary)
    report={'schema':'cicadaport_p0a5_udp_s7_cell_v1','head':HEAD,
            'binary_sha256':args.expected_sha256,'host':host,'capabilities':caps,
            'negative_cases':negative,'loopback_echo':positive,
            'external_network':False,'no_public_selector':True,'no_git_writes':True,
            'g8_live':'NO_GO_OPERACIONAL','status':'PASS_LOCAL_UDP_CELL'}
    with output.open('x',encoding='utf-8') as file:
        json.dump(report,file,indent=2,sort_keys=True);file.write('\n')
    output.chmod(0o600)
    print('P0A5_S7_CELL=PASS_LOCAL_UDP_ECHO:'+host['matrix_cell']+':MATRIX='+str(host['is_matrix_cell']))
    print('P0A5_S7_CELL_REPORT='+str(output))
    return 0
def main():
    try:return run()
    except (Stop,OSError,ValueError,json.JSONDecodeError,subprocess.TimeoutExpired) as err:
        print('P0A5_S7_CELL=STOP:'+str(err).replace('\n',' ')[:500],file=sys.stderr)
        return 1
if __name__=='__main__':sys.exit(main())
