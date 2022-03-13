#!/usr/bin/env python
import subprocess

import argparse
import os
import time

from pyngrok import ngrok


def main():
    parser = argparse.ArgumentParser(description="Uploader")
    parser.add_argument(
        "--port", "-p",
        type=int,
        help="Port to listen on",
        default=2006,
    )
    args = parser.parse_args()
    here = os.path.dirname(os.path.abspath(__file__))
    proc = subprocess.Popen(
        f'python fileserver.py --port {args.port}', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, cwd=here, shell=True)

    try:
        ngrok_tunnel = ngrok.connect(3306, "http")
        print(f"  LOCAL:  http://127.0.0.1:{args.port}")
        print(f"\nFILESERVER:\n  PUBLIC: {ngrok_tunnel.public_url}")
        while True:
            time.sleep(.1)
    except KeyboardInterrupt:
        pass

    finally:
        proc.kill()


if __name__ == '__main__':
    main()
