def variable_func(*number):
	for i in number:
		print(i)

def keyword_func(age, **kw):
	print('age:', age, 'other:', kw)

def define_kw_func(age,*,country, city):
	print('age:',age, 'country:', country, 'city:', city)

variable_func([1,2,3])
keyword_func(1, city ='nb')
kw_dict = {'country':'china', 'city':'nb', 'name':None}
define_kw_func(2, country='china', city='nb')