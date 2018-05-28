# 定义函数： def
# 

def my_abs(x):
	if not isinstance(x, (int, float)):		# 参数类型检查
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x


print(my_abs(-8))


# 定义空函数，pass
def nop():
	pass

# pass 代表占位符，还可以用在其他语句里


# 数据类型检查， isinstance()
# print(my_abs('a'))


# 返回多个值
import math	# 导入 math包

def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# 实际函数返回的仍是单一值，tuple，但是在语法上，返回一个tuple可以省略 括号
r = move(100, 100, 60, math.pi / 6)
print(r)


# 练习
# 
def quadratic(a, b, c):
	if a == 0:
		return - (c / b)
		
	delta = pow(b, 2) - 4 * a * c
	if delta < 0:
		return None
	elif delta == 0:
		return - (b / (2 * a))
	else:
		x1 = ((-b) + math.sqrt(delta)) / (2 * a)
		x2 = ((-b) - math.sqrt(delta)) / (2 * a)
		return x1, x2

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')