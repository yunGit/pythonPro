# 
# 	递归函数
# 	
def fact(n):
	if n == 1:
		return 1
	return n * fact(n-1)

# print(fact(900))
# print(fact(1000))		# 栈溢出

# 
# 	优化：递归尾调用(前提是解释器根据尾递归调用做了优化)
# 	即函数返回时调用自身，并且，return语句不包含表达式
# 	为了解决递归调用栈溢出问题
def factTail(n, product):
	if n == 1:
		return product
	return factTail(n - 1, n * product)

# print(factTail(900, 1))


# 汉诺塔
# 
def move(n, a, b, c):
	if n == 1:
		print(a, '-->', c)
		return
	else:
		move(n-1, a, c, b)
		move(1, a, b, c)
		move(n-1, b, a, c)

print('move 1--------------------------')
move(1, 'a', 'b', 'c')
print('move 2--------------------------')
move(2, 'a', 'b', 'c')
print('move 3--------------------------')
move(3, 'a', 'b', 'c')