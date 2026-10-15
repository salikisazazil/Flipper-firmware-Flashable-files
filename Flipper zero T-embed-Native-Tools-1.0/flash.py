#!/usr/bin/env python3
"""Verify this release and flash only when an explicit serial port is supplied."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', help='Serial port, for example COM5 or /dev/ttyACM0')
    parser.add_argument('--baud', type=int, default=460800)
    parser.add_argument('--verify-only', action='store_true')
    args = parser.parse_args()
    if not args.verify_only and not args.port:
        parser.error('--port is required unless --verify-only is selected')
    root = Path(__file__).resolve().parent
    manifest = json.loads((root / 'release-manifest.json').read_text())
    files = manifest['flash_files']
    for item in files:
        p = root / item['path']
        data = p.read_bytes()
        if len(data) != item['bytes'] or hashlib.sha256(data).hexdigest() != item['sha256']:
            raise SystemExit('Verification failed: ' + item['path'])
        print('Verified:', item['path'], 'at', item['offset'], flush=True)
    if args.verify_only:
        return 0
    command = [sys.executable, '-m', 'esptool', '--chip', 'esp32s3',
               '--port', args.port, '--baud', str(args.baud),
               '--before', 'default_reset', '--after', 'hard_reset',
               'write_flash', '--flash_mode', 'dio', '--flash_freq', '80m',
               '--flash_size', '16MB']
    for item in files:
        command.extend([item['offset'], str(root / item['path'])])
    return subprocess.call(command)

if __name__ == '__main__':
    raise SystemExit(main())
