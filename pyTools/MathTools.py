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

# 获得矩阵某一列
def GetColumnOfMatrix(matrix, index):
	rowNum = len(matrix)
	colNum = len(matrix[0])

	if colNum < (index+1):
		 return None, False, "colNum < index+1"

	column = []
	i = 0
	while i < rowNum:
	 	column.append(matrix[i][index])

 	return column, True, ""


# 矩阵追加列
def AppendColumnToMatrix(matrix, column):
	rowMatrixNum = len(matirx)
	rowColumnNum = len(column)

	# 空矩阵
	if rowMatrixNum == 0:
		i = 0
		while i < rowColumnNum:
			matrix.append([])

	colMatrixNum = len(matrix[0])

	if rowMatrixNum != rowColumnNum:
		return None, False, "rowMatrixNum != rowColumnNum"

	i = 0
	while i < rowMatrixNum:
		matrix[i].append(column[i])

	return matrix, True, ""


# 获得矩阵某一行
def GetRowOfMatrix(matrix, index):
	rowNum = len(matrix)
	colNum = len(matrix[0])

	if rowNum < (index+1):
		 return None, False, "rowNum < index+1"

	return matrix[index]


# 求解向量乘向量 vA * vB
def VectorVectorProduct(vectorA, vectorB):
	columnVectorANum = len(vectorA)
	rowvectorBNum = len(vectorB)

	if columnVectorANum != rowvectorBNum:
		return None, False, "columnVectorANum != rowvectorBNum"

	product = 0
	i = 0
	while i < columnVectorANum:
		product += (vectorA[i] * vectorB[i])
		i += 1;
	return [product], True, ""


# 求解矩阵乘向量 Matrix * Vector
def MatrixVectorProduct(matrix, vector):
	rowMatrixNum = len(matrix)
	columnMatrixNum = len(matrix[0])
	rowVectorNum = len(vector)

	if columnMatrixNum != rowVectorNum:
		return None, False, "columnMatrixNum != rowVectorNum"

	product = []
	tmpProduct = 0
	i = 0
	while i < rowMatrixNum:
		tmpProduct = VectorVectorProduct(matrix[i], vector)
		product.append(tmpProduct[0][0])
		i += 1
	return product, True, ""


# 求解向量乘矩阵 Vector * Matrix
def VectorMatrixProduct(vector, matrix):
	# columnVectorNum = len(vector)
	# rowMatrixNum = len(matrix)
	# columnMatrixNum = len(matrix[0])

	# if rowMatrixNum != columnVectorNum:
	# 	return None, False, "rowMatrixNum != columnVectorNum"

	# product = []
	# tmpProduct = 0
	# i = 0
	# while i < columnMatrixNum:
	# 	tmpProduct = VectorVectorProduct(matrix[i], vector)
	# 	product.append(tmpProduct[0][0])
	# 	i += 1
	# return product, True, ""


matirx = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
vector = [1, 2, 1]

product, isOk, errStr = MatrixVectorProduct(matirx, vector)
print(product, isOk, errStr)