#
# 有内置的一种数据类型是列表 list, 有序集合
# 

classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
l = len(classmates)
print(l)

print(classmates[0])
# print(classmates[3])
print(classmates[-1])

# append()
classmates.append('Adam')
print(classmates)

# pop()
classmates.pop()
print(classmates)
classmates.pop(0)
print(classmates)

classmates[0] = "zhangsan"
print(classmates)

# list 元素类型可以不同
L = ['Apple', 123, True, 789]
S = ['python', 'java', L, 'Scheme']
print(S, len(S))
print(L, len(L))



# 另一种有序列表叫元组：tuple，一旦初始化不能改变
classmatesT = ('Michael', 'Bob', 123, 'Tracy', 890)
print(classmatesT)

# classmatesT[0] = 'zhangsan' # 报错
print(classmatesT)

# 但是，若定义只有一个元素的tuple
t = (1) # 此处定义的 t 非 tuple， 而是 1
print(t)
tt = (1,) # 此处定义的为 tuple
print(tt)

T = [
	['Apple', 'Google','Microsoft'],
	['Java', 'Python', 'Ruby', 'PHP'],
	['Adam', 'Bart', 'Lisa']
]

print(T[0][0])
print(T[1][1])
print(T[2][2])