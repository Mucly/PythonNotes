def variableFunc(*number):  # 将所有实参变为一个tuple
    '''可变参数'''
    for i in number:
        print(i)


def kwFunc(age, **kw):
    '''关键字参数'''
    print('age:', age, 'other:', kw)


def namedkwFunc(age, *, country, city):
    '''命名关键字参数'''
    print('age:', age, 'country:', country, 'city:', city)


list1 = [1, 2, 3]
kw_dict = {'country': 'china', 'city': 'nb', 'name': None}

variableFunc(*list1)  # 将list1拆解为1, 2, 3 后传入到函数内  output: 1,2,3
variableFunc(list1)  # 直接将list1传入到函数内  output: [1, 2, 3]
kwFunc(1, city='nb')  # output: age: 1 other: {'city': 'nb'}
namedkwFunc(2, country='china', city='nb')  # output: age: 2 country: china city: nb
