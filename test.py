import sys
import subprocess

for line in open(sys.argv[1]):
    line = line.strip()
    cmd = ['./main.py', '-predict="' + line + '"']
    # cmd += line
    # cmd += '"'
    subprocess.run(cmd)