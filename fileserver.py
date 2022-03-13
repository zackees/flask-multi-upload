#!/usr/bin/env python

import argparse

def main():
    from uploadr.app import app
    parser = argparse.ArgumentParser(description="Ngrok Uploadr")
    parser.add_argument(
        "--port", "-p",
        type=int,
        help="Port to listen on",
        default=2006,
    )
    args = parser.parse_args()
    flask_options = dict(
        host='0.0.0.0',
        debug=True,
        port=args.port,
        threaded=True,
    )
    app.run(**flask_options)


if __name__ == '__main__':
  main()
    
