import subprocess

"""
order = subprocess.Popen('diroo',
                         shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE
                         )

res = order.stdout.read().decode('gbk')
print(res)

print('==============================')

res = order.stderr.read().decode('gbk')
print(res)

"""

order = subprocess.run('dir',
                       shell=True,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE
                       )

res = order.stdout.decode('gbk')
print(res)

print('==============================')

res = order.stderr.decode('gbk')
print(res)


