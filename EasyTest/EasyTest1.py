# -*- coding:utf-8 -*-
# 

# 九九乘法表
def NineNineFormula():
	lines = ''
	for x in range(1, 10):
		line = ''
		for y in range(1, 10):
			if x <= y:
				one = '%d x %d = %2d 	' %(x, y, x*y)
				line = line + one
		lines = lines + line + '\n'
	print(lines)

NineNineFormula()

# 冒泡排序
def Sort1(*tup):
	aList = list(tup)
	i = 0
	while i < len(aList):
		j = i + 1
		while j < len(aList):
			if aList[i] > aList[j]:
				r = aList[j]
				aList[j] = aList[i]
				aList[i] = r
			j = j + 1
		i = i + 1
	return aList

# 数组倒置
def Sort2(*tup):
	aList = list(tup)
	list_len = len(aList)
	l_len = list_len//2
	for i in range(l_len):
		aList[i], aList[list_len-1-i] = aList[list_len-1-i], aList[i]
	return aList


print(Sort1(1,9,5,3,8,5,10))
print(Sort2(1,9,5,3,8,5,10))

# 斐波那契数列
def Fibonacci(length):
	pass

# Fibonacci(10)
