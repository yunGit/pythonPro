# -*- coding: utf-8 -*-

#
# 条件判断
# 

age = 20
print("your age is ", age)
if age >= 18:
	print("adult")
elif age >= 6:
	print("teenager")
else:
	print("kid")

if age:
	print("age ", age)


# input() - 读取用户输入
birth = input('birth: ')
# int() - 类型转换
birth = int(birth)
if birth < 2000:
	print("00前")
else:
	print("00后")


height = input("height(m) 	:")
weight = input("weight(kg) 	:")

height = float(height)
weight = float(weight)

bmi = weight / (height * height)
print("your BMI is: %.2f" % bmi)

if bmi < 18.5:
	print("Too Slight")
elif bmi < 25:
	print("Normal")
elif bmi <28:
	print("Too Weight")
elif bmi < 32:
	print("Fat!")
else:
	print("Too Fat!!!")