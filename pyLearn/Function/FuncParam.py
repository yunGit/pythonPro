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