# 
# 	切片
# 	取一个list或tuple的部分元素
# 	

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 笨方法
l1 = [L[0], L[1], L[2]]
print(l1)

# 切片
l2 = L[0:3]		# 表示从索引0开始取， 直到索引 3 为止，但不包括索引 3
print(l2)

l3 = L[:1]		# 如果第一个索引是 0，还可以省略
print(l3)

l4 = L[-1:]		# 倒数切片, 记住倒数第一个元素的索引是 -1
print(l4)

LL = list(range(100))

# 前10个数，每两个取一个
ll1 = LL[:10:2]
print(ll1)

# 所有数，每5个取一个
ll2 = LL[::5]
print(ll2)

# tuple取切片操作之后的结果仍是 tuple
T = tuple(range(10))

t1 = T[:3]
print(t1)

# 字符串也可以被看成是一种 list，操作结果仍然是 字符串
S = 'ABCDEFG'

s1 = S[:3]
print(s1)

def trim(s):
	while s[:1] == ' ' or s[-1:] == ' ':
		if s[:1] == ' ':
			s = s[1:]
		if s[-1:] == ' ':
			s = s[:-1]
	
	return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
