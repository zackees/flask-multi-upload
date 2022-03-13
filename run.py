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
        public_url = "Not available"
        try:
            ngrok_tunnel = ngrok.connect(args.port, "http")
            public_url = ngrok_tunnel.public_url
        except Exception as e:
            print(f"{__file__}: Couldn't open up ngrok tunnel because {e}")
        print(
            "UPLOAD SERVER:\n"
            f"  LOCAL: http://127.0.0.1:{args.port}\n"
            f"  PUBLIC: {public_url}"
        )
        while True:
            time.sleep(.1)
    except KeyboardInterrupt:
        pass

    finally:
        proc.kill()


if __name__ == '__main__':
    main()
