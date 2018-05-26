#
# python 的循环有两种
# 
# 一种是: for ... in 循环，依次把 list 或 tuple 中的每个元素迭代出来
# 第二种是：while 循环，只要条件满足则不断循环
# 
# 
names = ["Michael", "Bob", "Tracy"]
for name in names:
	print(name)

sum = 0;
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
	sum = sum + x

print(sum)

# range() - 可以生成一个整数序列
l = list(range(101))
sum = 0
for x in l:
	sum += x

print(sum)

# while
sum = 0
n = 99
while n > 0:
	sum = sum + n
	n = n - 2
print(sum)

# break
# 
n = 1
while n <= 100:
	if n > 10:
		break
	print(n)
	n += 1
print("END")

# continue
n = 0
while n < 10:
	n += 1
	if n %2:
		continue
	print(n)