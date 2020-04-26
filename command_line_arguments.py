# python can run any process in the terminal

import subprocess
import time

from subprocess import PIPE


completed = subprocess.run(["ls", "-l"], stdout=PIPE)

print("args", completed.args)
print("return_code", completed.returncode)
print("std_err", completed.stderr)
print("std_out", completed.stdout.decode())

completed2 = subprocess.run(["python3", "/home/elsys/PycharmProjects/mosh_python_2020/python_run_terminal.py"], stdout=PIPE)
time.sleep(1)
print("std_out", completed2.stdout.decode())

