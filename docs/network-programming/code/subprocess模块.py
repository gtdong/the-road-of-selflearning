import subprocess


cmd = subprocess.Popen('dir',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
stdout = cmd.stdout.read().decode('gbk')
stderr = cmd.stderr.read().decode('gbk')
print(stdout+stderr)