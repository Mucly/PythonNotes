# 文件IO操作
f = open('path/to/file', 'r', encording = 'UTF-8', error = 'ignore')	#r，rb，w，wb
f.close()

with open('path/to/file', 'r') as f:	#自动调用close()
	pass

f.readline()	#每次读一行内容
f.readsize(num)	#每次读num个字节，缺省读所有内容
f.readlines()	#读所有内容

from io import StringIO
f = StringIO()
f.write('a')
f.getvalue() #>>>abc

from io import BytesIO
f = BytesIO()