# 
# 	迭代
# 	for ... in
# 	不仅可以用在 list 或 tuple 上，还可以作用在 其他可迭代对象上，譬如 dict
# 	因为 dict 的存储不是按照 list 的方式允许排列，所以迭代出的结果顺序很可能不一样
# 	默认情况下， dict 迭代的是 key，如果要迭代 value，可以用 for value in d.values()， 如果同时 key和 value，则 for k,v in d.items()
# 	对于如何判断一个对象是否可迭代对象， collections模块的 Iterable类型判断

from collections import Iterable
canIter = isinstance('abc', Iterable)		# str 是否可迭代
print(canIter)
canIter = isinstance(123, Iterable)
print(canIter)
canIter = isinstance([1,2,3], Iterable)
print(canIter)


def findMinAndMax(L):
	if len(L) == 0:
		return (None, None)
	min = L[0]
	max = L[0]
	for x in L:
		if min > x:
			min = x
		if max < x:
			max = x
	return (min, max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')