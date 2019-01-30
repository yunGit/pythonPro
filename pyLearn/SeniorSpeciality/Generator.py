# 	
# 	生成器
# 	
# 一边循环一边计算的机制，成为生成器：generator
# 方法一：只要把一个列表生成式的[] 改成()
L = [x * x for x in range(10)]
print(L)

g = (x * x for x in range(10))
print(g)
print(next(g))	# 可以通过 next() 函数获得 generator的下一个返回值

for n in g:
	print(n)