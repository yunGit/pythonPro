#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 字符和编码
# 
# ASCII, A  - 65,  z - 122
# 
# GB2312 	- 中文
# Shift_JIS - 日文
# Euc-kr	- 韩文
# 
# Unicode	- 统一所有语言
# 	最常用的是 两个字节表示一个字符，偏僻的用四个字节
# 	
# 	
# 	UTF-8编码 - "可变长的Unicode编码"
# 		常用的 英文字母 - 1个字节
# 				汉字通常 - 3个字节
# 				生僻字符 - 4，6个字节
# 				
# 	
# 	内存中统一使用 Unicode 编码， 需要存盘时转换为 UTF-8编码
# 	

print("中文")

print(ord('A'))		# ord() - 获取字符的整数表示
print(ord('中'))	

print(chr(20013))	# chr() - 把编码转换为对应的字符串
print(chr(65))


# 网络传输 将 str类型转换为 bytes 类型，每个字符只占一个字节

x = b'ABC'	# 用带 b 前缀的 引号表示 betes类型

ascAbc = 'ABC'.encode('ascii')		# encode() - 可以把 str 转换为 bytes
print(ascAbc)

utf8Str = '中文'.encode('utf-8')
print(utf8Str)

unicodeAbc = ascAbc.decode('ascii')	# decode() - 反转 encode
print(unicodeAbc)

unicodeStr = utf8Str.decode('utf-8')
print(unicodeStr)

print(len(utf8Str))					# len() - 获取字符长度
print(len(unicodeStr))

# 文件第二行 # -*- coding: utf-8 -*-  - 标志utf编码
# 

# 格式化输出字符串
# % 实现连接
# %d - 整数
# %f - 浮点数
# %s - 字符串
# %x - 十六进制整数

print('hello , %s' % 'world')
print('hi, %s, you have $%2d., PI is %.2f' % ('Michael', 10000, 3.1415926))