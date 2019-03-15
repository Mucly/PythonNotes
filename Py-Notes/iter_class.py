class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1
	def __iter__(self):		#定义一个迭代方法，返回一个迭代对象，需和__next__配合
		return self
	def __next__(self):		#定义__next__方法，处理迭代规则
		self.a, self.b = self.b, self.a + self.b
		if self.a > 100000:
			raise StopIteration()
		return self.a

for n in Fib():
	print(n)