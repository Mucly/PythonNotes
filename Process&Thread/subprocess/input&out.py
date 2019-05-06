import subprocess

print('$ ping')
p = subprocess.Popen(['ping'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'www.baidu.com -n 1\n')
print(output.decode("gbk"))
# print('Exit code:', p.returncode)
