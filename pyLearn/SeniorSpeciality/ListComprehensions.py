# 
# 	是python内置的非常简单却很强大的可以用来创建 list 的生成式
# 	

print(list(range(1, 11)))

# 
# 生成[1x1, 2x2, 3x3, ... , 10x10]
# 
# 方法一
L = []
for x in range(1, 11):
	L.append(x * x)

print(L)

# 方法二，列表生成式
print([x * x for x in range(1, 11)])

# 还可以筛选偶数
print([x * x for x in range(1, 11) if x % 2 == 0])

# 生成全排列
print([m + n for m in 'ABC' for n in 'XYZ'])


# 列出当前目录下的所有文件和目录名
import os	# 导入os模块，模块的概念后面讲到
print([d for d in os.listdir('/')])	# os.listdir() 可列出文件和目录

# 因为 for 循环可以同时使用两个甚至多个变量，比如 dict的 items() 可以同时迭代 key和value
# 所以列表生成式也可以使用两个变量来生成list
d = {'x':'A', 'y':'B', 'z':'C'}
print([k + ' = '+ v for k, v in d.items()])

# 把一个list中所有的字符串变成小写
LS = ['Hello', 'World', 'IBM', 'Apple', 19, None]
print([s.lower() for s in LS if isinstance(s, str)])



