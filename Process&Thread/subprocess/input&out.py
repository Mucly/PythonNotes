# -*- coding:utf-8 -*-
import subprocess

# 等同于cmd执行 nslookup www.python.org
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)
