import os
'''默认path为当前'''
'''系统相关'''
os_name 			= os.name 				#os类型，nt = windows， posix = others
os_environ 			= os.environ			#获得环境变量
os_environ_get_key  = os.environ.get('OS')	#获得环境变量中key为os的值
'''操作文件和目录'''
os_path_abspath 	= os.path.abspath('.')	#查看当前目录的绝对路径
os_path_join 		= os.path.join('/Users/wuxz/Desktop/py', 'testdir') #告知新目录testdir的完整路径，windows下返回
os_path_split		= os.path.split('/Users/wuxz/Desktop/py/1.txt')	#返回'path', '1.txt'
os_path_splitext	= os.path.splitext('/Users/wuxz/Desktop/py/1.txt') #返回'path', '.txt'
os_path_mkdir		= os.mkdir('/Users/wuxz/Desktop/py/testdir')
os_path_rmdir		= os.rmdir('/Users/wuxz/Desktop/py/testdir')

[x for x in os.listdir('.') if os.path.isdir(x)]	#罗列当前路径下所有dir
[x for x in os.listdir('.') if os.path.isfile(x) and
os.path.splitext(x)[1]=='.py']						#罗列.py文件

os_rename			= os.rename('1.png', '/Users/wuxz/Desktop/test.py') #rename并移动至后者path
os_remove			= os.rename('/Users/wuxz/Desktop/py/1.txt')