import os
from subprocess import Popen, PIPE
import os

cwd = os.getcwd()
for filename in os.listdir('.'):
    print(filename)
    if filename != '__init__.py':
        cmd_line = os.path.join(cwd, filename)
        cmd = ["python", cmd_line]
        output = Popen(cmd, stdout=PIPE).communicate()[0]
        print(output)
