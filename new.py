#! /usr/bin/env python

import argparse
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor

TARGET_PROBLEMS = ['a', 'b', 'c', 'd', 'e']
SRC_TEMPLETE = 'template.exs'

parser = argparse.ArgumentParser()
parser.add_argument('contest', type=str, help='contest name')
args = parser.parse_args()

# prepare dirs
os.makedirs(args.contest, exist_ok=False)
for problem in TARGET_PROBLEMS:
    os.makedirs(f'{args.contest}/{problem}', exist_ok=False)
    os.makedirs(f'{args.contest}/{problem}/test', exist_ok=False)
    cmd = f'cp {SRC_TEMPLETE} {args.contest}/{problem}/main.ex'
    subprocess.run(cmd, shell=True)

# download testcases
with ThreadPoolExecutor(max_workers=10) as executor:
    for problem in TARGET_PROBLEMS:
        executor.submit(subprocess.run, f'oj d -d {args.contest}/{problem}/test https://atcoder.jp/contests/{args.contest}/tasks/{args.contest}_{problem}', shell=True)