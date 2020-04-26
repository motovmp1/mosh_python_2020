# python can run any process in the terminal

import subprocess
import time

from subprocess import PIPE


completed = subprocess.run(["ls", "-l"], stdout=PIPE)

print("args", completed.args)
print("return_code", completed.returncode)
print("std_err", completed.stderr)
print("std_out", completed.stdout.decode())


# always need to check is the system fail or not
completed2 = subprocess.run(["python3", "/home/elsys/PycharmProjects/mosh_python_2020/python_run_terminal.py"], stdout=PIPE)
time.sleep(1)
print("std_out", completed2.stdout.decode())
print("return_code", completed2.returncode)
if completed2.returncode != 0:
    print(completed2.stderr)
else:
    print("PASS")

