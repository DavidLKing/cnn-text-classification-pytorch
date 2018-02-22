import sys
import subprocess
import pdb

for line in open(sys.argv[1]):
    line = line.strip()
    # cmd = ['./main.py', '-predict="' + line + '"']
    cmd = ['./main.py', '-snapshot=good.pt',
           '-kernel-sizes', '1,2,3,4,5', '-predict="' + line + '"']
    # pdb.set_trace()
    # cmd += line
    # cmd += '"'
    subprocess.run(cmd)