import subprocess

a = subprocess.run('tracert  195.78.54.143', shell=True, stdout=subprocess.PIPE)
print(a)
