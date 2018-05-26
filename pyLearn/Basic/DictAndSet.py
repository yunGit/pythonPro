# 
# 字典 dict

d = {'Michael':95, 'Bob':75, 'Tracy':85}
print(d['Bob'])
d['Adam'] = 67
print(d['Adam'])

# 一个 key 智能对应一个 value
# 多次对一个 key 放入 value， 后面的值会把前面的值冲掉
d['Adam'] = 90
print(d['Adam'])

# 如果 key 不存在， 报错
# print(d['zhang'])
# 
# 通过 in 判断是否 key 存在
print('zhang' in d)

# 通过 get() ，如果key不存在，则返回 None， 或者返回自己指定的 value
print(d.get('zhang'))
print(d.get('zhang', -1))

# 通过 pop()，删除元素
print(d.pop('Adam'))
print(d)

# 和 list 比较的 dict 特点
# 1. 查找和插入的速度极快，不会随着key 的增加而变慢
# 2. 需要占用大量的内存，内存浪费多
# 故，是在用空间换区时间
# 
# 注意：**************dict 的 key 必须是不可变对象***************
# 因为通过哈希算法（Hash）根据 key 计算value的存储位置，如果每次计算key的结果不同，则dict内部就完全混乱了
# 在 python 中，字符串、整数等都是不可变的，而因为list是可变的，故不能作为key
# 对于不可变对象来说，调用对象自身的任意方法，也不会改变改对象自身的内容。
# 相反，这些方法会创建新的对象并返回，这样就保证了不可变对象本身永远是不可改变的
# 
# 
# key = [1, 2, 3]
# d[key] = 'a list'
# print(d)
# 


# set
# 
# set 和 dict类似，但不存储 value,在set中也没有重复的 key
# 要创建一个 set ，需要提供一个 list 作为输入集合
s = set([1, 2, 3, 4, 1, 3])
print(s)	# 显示的顺序不代表 set是有序的， 重复元素自动被过滤

# add() - 添加元素
s.add(4)
print(s)

# remove() - 删除元素
s.remove(4)
print(s)

# & - 交集
# | - 并集
# 
s1 = set([1, 2, 3])
s2 = set([2, 3, 5])
print(s1 & s2)
print(s1 | s2)