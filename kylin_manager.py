#!/usr/bin/env python
# -*- coding: utf-8 -*-


import argparse
import kylin
import json

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', required=True)
    parser.add_argument('--port', type=int, default=7070)
    parser.add_argument('--username', required=True)
    parser.add_argument('--password', required=True)
    subparsers = parser.add_subparsers()

    exception_job_parser = subparsers.add_parser('exception-job',
                                                 help='get jobs which status is error or duration time exceed the max-duration')
    exception_job_parser.add_argument("--max-duration", type=int, required=True,
                                      help='filter the job which duration time exceed this value in seconds')
    exception_job_parser.set_defaults(func=kylin.exception_job)

    args = parser.parse_args()
    output = args.func(**vars(args))
    print json.dumps(output, indent=4)
