# 一、类型和变量

print ('''helo \n
python''')

a = 100

if a > 0:
	print (a)
else:
	print (-a)

print(True)

b = False
print(b)

print(b or True)

print(not b)

n = None
print(n)

# 全部大写的变量名表示常量，约定俗成
PI = 3.1415926
print(PI)
PI = 5
print(PI)

# 整数的地板除//永远是整数, 只取结果的整数部分
c = 10 / 3
print(c)
c = 10 // 3
print(c)
d = 10 % 3
print(d)

# -*- coding: utf-8 -*-
n = 123
f = 456.789
s1 = 'Hello, world'	
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)

# 对变量赋值x = y是把变量x指向真正的对象，该对象是变量y所指向的。随后对变量y的赋值不影响变量x的指向
# Python的整数没有大小限制
# Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）
# 
# r'' 表示字符串内的字符默认不转义
# '''...'''	 表示多行内容