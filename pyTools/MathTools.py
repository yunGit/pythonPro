# 
# Something tools for math
# 

import math	# 导入 math包

# 求解一元二次方程组
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
