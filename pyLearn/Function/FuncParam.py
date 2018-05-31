#
#  		默认参数
#   
#     函数默认参数必须牢记一点：默认参数必须指向不变对象！
# 例如: str, None
# 因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误
# 此外，由于对象不变，多任务环境下同事读取对象不需要加锁，同时读一点问题都没有
# 示范反例：
def add_end(L=[]):
	L.append('END')
	return L

add_end()
l = add_end()
print(l) # 这里会打印['END', 'END']而不是 ['END']

# 使用默认参数可以指定参数名字调用
# 
def enroll(name, gender, age = 6, city = 'Beigjing'):
	print('name is :', name)
	print('gender is :', gender)
	print('age is :', age)
	print('city is :', city)

enroll('zhangsan', 'F')
enroll('Lisi', 'A', city = 'Tianjin')   # city is : Tianjin


# 
# 		可变参数
# 		
# 	把参数作为一个 list 或 tuple 传进来
# 	定义可变参数，只需在参数前面加 *
def cale(numbers):
	sum = 0
	for n in numbers:
		sum += n * n
	return sum

def cale2(*numbers):
	sum = 0
	for n in numbers:
		sum += n * n
	return sum

print(cale([1, 2, 3]))
print(cale([1, 2, 3, 4]))

print(cale2(1, 2, 3, 4, 5))		# 调用的可变参数函数 cale2()

nums = [1, 3, 5, 7]
print(cale2(*nums))

# 
# 		关键字参数
# 		
# 	关键字参数在函数内部自动组装成为一个 dict
# 	只需在参数前面加  **
# 	
def person(name, age, **kw):
	print('name: ', name, ' age: ', age, ' other: ', kw)

person('Michael', 30)
person('Bob', 35, city = 'Beigjing', job='Engineer')

# 
# 如果要限制关键字参数的名字，则可以用命名关键字参数，需要一个特殊分隔符 * , * 后面的参数被视为命名关键字参数
# 命名关键字参数调用时必须传入参数名，否则报错
# 
def person2(name, age, *, city, job):
	print(name, age, city, job)

person2('Jack', 24, city='Beigjing', job='Engineer')
# person2('hi', 1, 'beijing', 'chushi')


# 
# 		参数组合
# 		
# 	定义函数时，必选参数、默认参数、可变参数、关键字参数和命名关键字参数，可以组合使用
# 	注意：参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
# 	
def f1(a, b, c=0, *, d, **kw):
	print('a = ', a, ', b = ', b, ', c = ', c, ', d = ', d, ', kw = ', kw)
def f2(a, b, c=0, *args, **kw):
	print('a = ', a, ', b = ', b, ', c = ', c, ', args = ', args, ', kw = ', kw)

f1(10, 5, 8, d=0)
f2(10, 5, 3, 9, 90, 40, r=10)

def product(x, y=1, *args):
	pro = 1
	for v in args:
		pro *= v
	return x * y * pro

# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')