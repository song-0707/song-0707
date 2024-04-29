# 1.0 输出 print()

# print('Hello World')  # Hello World
# print('Hi Python', 123432)   # Hi Python, 123432

# 1.1 python 换行
# print('Hi', end='\n')  # python 输出默认自动换行  \n -> 换行的意思
# print('Hi', end='')
# print('Hello World')  # 输出结果就是两个内容在同一行  Hi Hello World

# 1.2 格式化输出 variable
# age, name = 10, 'Bob'
# print(name, age)    # Bob 10
# print('name: {}, age: {}'.format(name, age))    # name: Bob, age: 10
# print(f'name: {name}, age: {age}')   # name: Bob, age: 10


# 2.0 输入 input()  -> 从终端接受用户输入 给代码
# age = input('请输入年龄: ')
# print(age)         # 用户输入的数据大部分都是str(字符串)


# input 实例
# username = input('请输入用户名: ')
# passwd = input('请输入密码: ')
# if username == 'bob' and passwd == '123':   # 这里123放''(引号)是因为用户输入的数据属于str
#     print('登录成功')
# else:
#     print('登录失败')


# 3.0 变量名
# 不可以和python关键字起冲突
# 不可以数字开头


# 4.0 int 整数
# a = 123
# print(type(a))  # <class 'int'>


# 5.0 float 浮点数/小数
# a = 3.141592654
# print(type(a))   # <class 'float'>

# 5.1.1 四舍五入 round()  -> 保留0位小数
# num = 3.141592654
# res = round(num)
# print(res)    # 3

# 5.1.2 保留三位小数
# res = round(num, 3)    # -> 数字= 保留多少位小数
# print(res)    # 3.142

# 5.2 加减乘除
# a = 3
# b = 10
# print('{} + {} = {}'.format(a, b, a+b))    # 3 + 10 = 13
# print('{} - {} = {}'.format(a, b, a-b))    # 3 - 10 = -7
# print('{} * {} = {}'.format(a, b, a*b))    # 3 * 10 = 30
# print('{} / {} = {}'.format(a, b, a/b))    # 3 / 10 = 0.3

# 5.3 地板除 // (整除)  直接扔掉小数点
# a, b = 10, 3
# res = a // b    # 3
# print(res)

# 5.4 模运算 % 取余数
# a, b = 10, 3
# res = 10 % 3    # 1
# print(res)


# 案例: 取出不同number place的数字
# num = 4259
# a = num // 1 % 10      # 个位数
# b = num // 10 % 10     # 十位数
# c = num // 100 % 10    # 百位数
# d = num // 1000 % 10   # 千位数
# print(a, b, c, d)

# 5.5 更多的运算(math模块)
# import math
# math.log(2, 4)
# math.sin(50)
# math.cos(90)

# 5.6 绝对值
# n = -10
# res = abs(n)   # 10


# 6.0 Bool  取值只能是True 或者 False
# label = True
# print(type(label))    # <class 'bool'>
# print(1 == 1)   # True
# print(1 > 2)    # False
# print(2 >= 2)   # True
# print(2 != 3)   # True


# 7.0 str  单引号'' 或者双引号"" 包起来的
# s = 'hello world'
# print(type(s))      # <class 'str'>

# 7.1 请求字符串的长度  len()
# s = 'hello world'
# res = len(s)
# print(res)    # 11  空格也算一个字符

# 7.2 字符串取出某个字符  取出e
# print(s[1])    # e

# 7.3 取出一个片段
# 7.3.1 取出'llo'
# res = s[2:5]   # include left, exclude right
# print(res)    # llo

# 7.4 取出"hello"
# res = s[:5]  # 冒号前面留空代表从头开始        res = s[0:5:1]的结果是一样的
# print(res)    # hello

# 7.5 取出"world
# res = s[6:]   # 冒号后面留空代表读取到最后一个数据    # res = s[-5:] 的结果是一样的  意思是从倒数第五个到最后一个数据
# print(res)   # world

# 7.6 隔两个字符提取数据  [start:end:sep]  sep-> 分隔

# res = s[1:10:2]   # 第三个数字代表需要隔多少数字
# print(res)   # el ol

# res = s[10:1:-1]  # 这里的index根据数据一开始的排列  -1 代表倒着读取 但同时想读取的index也需要反过来写, 也就是大到小
# print(res)   # dlrow oll   'hello world'

# res = s[10:1:-2]  # 倒着并相隔两个值读取
# print(res)   # drwol

# 7.7 整个字符串倒过来写
# s = 'hello'
# res = s[::-1]
# print(res)    # olleh

# 7.8 找子串
# s1 = 'hello world hello'
# s2 = 'llo'
# res = s1.find(s2)   # find只会打印第一个见到的子串的index
# print(res)    # 2   这里的数字指的是index
#
# res = s1.find(s2, 3)    # 3指的是从第四个字符开始找起
# print(res)   # 14

# 7.9 替换部分片段 replace()  全局替换(绝大部分情况)
# s1 = 'hello world hello'   # 把llo替换成xxx
# s1 = s1.replace('llo', 'xxx')
# print(s1)

# s1 = s1.replace('llo', 'xxx', 1)   # 这里的1指的是只替换一次llo, 并非全局替换
# print(s1)

# start_index = s1.find('llo')   # 和上面的代码输出一样的结果
# end_index = start_index + len('llo')
# s1 = s1[:start_index] + 'xxx' + s1[end_index:]
# print(s1)

# 7.10 字符串的拼接
# s1 = 'hello'
# s2 = 'world'
# s3 = s1 + ' ' + s2
# print(s3)

# 7.11 lower() 转小写   upper() 转大写
# s1 = 'HELLO'
# s = s1.lower()
# print(s)  # hello
# s = s1.upper()
# print(s)   # HELLO

# 7.12 split() 把字符串根据特定的字符如空格或者其他符号拆分开来, 并放在list里面
# s = 'hello world i love'
# res = s.split(' ')
# print(res)    # ['hello', 'world', 'i', 'love']

# s = '1$2$234$23424'
# res = s.split("$")
# print(res)   # ['1', '2', '234', '23424']

# 7.13 strip() 对字符串的两端进行删除, ()里填写删除什么字符
# s = '$h$ello$$'
# res = s.strip('$')
# print(res)   # h$ello

# res = s.rstrip('$')
# print(res)   # $h$ello   对右边的尾端进行删除处理
#
# res = s.lstrip('$')
# print(res)   # h$ello$$  对左边的尾端进行删除处理

# \n
# s = s.strip('\n')

s = 'hello'
# print(s[0])   # 'h'
# print(s[10])   # IndexError: string index out of range

# print(s[1:3])        # el
# print(s[1:100])    # ello
# print(s[100:200])  # ''


# 8.0 list 列表
# mutable

# 可变类型: int, str, float, bool
# 不可变类型: list, dict  可以直接改变原本的内容, 且无需重新给变量名与赋值

# l1 = [32, 123, 4.1342, 'hello', [1, 2, 3], 32, 32, 100]

# 8.1 列表长度 len()
# print(len(l1))     # 8

# 8.2 增删改查

# 8.2.1 增加
# append() 末尾追加
# l1.append(110)
# print(l1)    # [32, 123, 4.1342, 'hello', [1, 2, 3], 32, 32, 100, 110]

# insert() 指定位置追加
# l1.insert(2, 99)   # 先写要在哪追加(index), 再写追加什么
# print(l1)

# 列表合并
# l1 = [32, 123, 4.1342, 'hello', [1, 2, 3], 32, 32, 100]
# l2 = [8, 9, 10]
# a) extend()
# l1.extend(l2)
# print(l1)     # [32, 123, 4.1342, 'hello', [1, 2, 3], 32, 32, 100, 8, 9, 10]

# b) +
# res = l1 + l2
# print(res)    # [32, 123, 4.1342, 'hello', [1, 2, 3], 32, 32, 100, 8, 9, 10]

# 8.2.2 删除
# l1 = [32, 123, 4.1342, 'hello', [1, 2, 3], 32, 32, 100]
# 指定值删除 remove  只移除了第一次出现的值
# l1.remove(32)
# print(l1)    # [123, 4.1342, 'hello', [1, 2, 3], 32, 32, 100]

# 把所有的32删掉
# n = l1.count(32)   # 计算有几个32
# for i in range(n):
#     l1.remove(32)
# print(l1)    # [123, 4.1342, 'hello', [1, 2, 3], 100]

# 指定位置删除    把2号位置的值删除
# l1 = [32, 123, 4.1342, 'hello', [1, 2, 3], 32, 32, 100]
# a) del()
# del l1[2]
# print(l1)   # [32, 123, 'hello', [1, 2, 3], 32, 32, 100]

# b) pop()   pop()只是把该位置的值弹出来
# l1.pop(2)
# print(l1)     # [32, 123, 'hello', [1, 2, 3], 32, 32, 100]

# res = l1.pop(2)
# print(res)     # 4.1342

# 8.2.3 改
# l1 = [32, 123, 4.1342, 'hello', [1, 2, 3], 32, 32, 100]
# l1[2] = 3.14     # 将index2, 第三个数据替换成3.14
# print(l1)

# l1[2] = [1, 2, 3]
# print(l1)   # [32, 123, [1, 2, 3], 'hello', [1, 2, 3], 32, 32, 100]   将index 2 的值替换成[1, 2, 3]

# 片段的替换
# l1[2:3] = [1, 2, 3]
# print(l1)   # [32, 123, 1, 2, 3, 'hello', [1, 2, 3], 32, 32, 100]   有加冒号的可以直接将列表内的元素直接放进去大列表里,
# 而没有冒号就是直接把整个列表当成一个元素放进去大列表

# 指定位置合并列表
# l1 = [32, 123, 4.1342, 'hello', [1, 2, 3], 32, 32, 100]
# l2 = [8, 9, 10]
# l1[2:2] = l2    # 这里两个index是一样的, 所以不会替换任何列表内的数据
# print(l1)   # [32, 123, 8, 9, 10, 4.1342, 'hello', [1, 2, 3], 32, 32, 100]

# res = l1[:2] + l2 + l1[2:]
# print(res)   # [32, 123, 8, 9, 10, 4.1342, 'hello', [1, 2, 3], 32, 32, 100]

# 8.2.4 查
# l1 = [32, 123, 4.1342, 'hello', [1, 2, 3], 32, 32, 100]
# print(l1[3])   # hello
# print(l1[10])   # IndexError: list index out of range

# res = l1[7:1:-2]
# print(res)   # [100, 32, 'hello']

# .index()
# res = l1.index(123)
# print(res)   # 1

# res = l1.index(200)
# print(res)   # ValueError: 200 is not in list   不存在

# 为了避免程序崩溃
# num = 200
# if num in l1:
#     res = l1.index(num)   # 如果列表内存在200, 返回200的index
# else:
#     res = -1   # 如果没有, 返回-1
# print(res)

# 案例 找出所有32的位置
# l1 = [32, 123, 4.1342, 'hello', [1, 2, 3], 32, 32, 100]
# num = 32
# n = l1.count(num)  # 次数
# result = []   # 保存结果
# start = 0    # 从0的位置开始找起
# for i in range(n):
#     if num in l1:
#         res = l1.index(32, start)
#         result.append(res)
#         start = res + 1
# print(result)

# 常用代码
# result = []
# for i in range(len(l1)):  # range(8)
#     if l1[i] == 32:
#         result.append(i)
# print(result)   # [0, 5, 6]

# 8.3 sort() 直接对原本的列表进行排列(默认小到大)   sorted() 相当于复制原本的列表并进行排序, 过后可找回原本的列表
# l1 = [12, 23, 42, 12, 53, 23, 54, 36, 10]
# l1.sort()
# print(l1)    # [10, 12, 12, 23, 23, 36, 42, 53, 54]

# l1.sort(reverse=True)
# print(l1)   # [54, 53, 42, 36, 23, 23, 12, 12, 10]

# res = sorted(l1)
# print(res)   # [10, 12, 12, 23, 23, 36, 42, 53, 54]
# print(l1)   # [12, 23, 42, 12, 53, 23, 54, 36, 10]

# 8.4 ASCII码
# 得到ascii值
# print(ord('a'))   # 97
# print(ord('b'))   # 98
# print(ord('0'))   # 48
# print(ord("A"))   # 65
# print(ord("B"))   # 66

# 8.5 字符串str 和 列表list 之间的关系
# l1 = ["h", "e", "l", "lo"]   # 前提是列表中的元素 必须都是str
# 1. list =》 str    join()
# res = '$'.join(l1)    join的格式: '两个字符串中间要用什么链接'.join
# print(res)   # h$e$l$lo

# # 2. str =》 list    split()
# res = res.split('$')    split的格式: xxx.split('根据什么字符来拆解字符串')
# print(res)   # ['h', 'e', 'l', 'lo']

# 9.0 dict 字典 {k:v, k:v, k:v...}   无需顺序
# 1. key必须唯一 不能重复, 必须是不可变类型  value是什么都行

# d = {"Bob": 100, 'Alice': 20, 'Tom': 50}
# print(type(d))    # <class 'dict'>
# print(len(d))   # 3

# 9.1 最常用的三种方法  后面遍历会用到
# print(list(d.keys()))    # ['Bob', 'Alice', 'Tom']
# print(list(d.values()))    # [100, 20, 50]
# print(list(d.items()))   # [('Bob', 100), ('Alice', 20), ('Tom', 50)]

# 9.2 增删改查
# 9.2.1 增加
# d = {"Bob": 100, 'Alice': 20, 'Tom': 50}
# 增加一个元素  'Jerry': 80
# d["Jerry"] = 80
# print(d)   # {'Bob': 100, 'Alice': 20, 'Tom': 50, 'Jerry': 80}

# 字典的合并  +并不能用在字典的合并
# d1 = {'Bob': 20, 'Alice': 50}
# d.update((d1))
# print(d)   # {'Bob': 20, 'Alice': 50, 'Tom': 50, 'Jerry': 80}

# 9.2.2 删除   删除key
# 1. del
# del d['Bob']
# print(d)   # {'Alice': 20, 'Tom': 50}

# 2. pop()
# res = d.pop('Bob')
# print(d)   # {'Alice': 20, 'Tom': 50}
# print(res)  # 100

# 9.2.3 修改
# d = {"Bob": 100, 'Alice': 20, 'Tom': 50}
# d['Bob'] = 20   # 修改
# print(d)    # {'Bob': 20, 'Alice': 20, 'Tom': 50, 'Jerry': 80}

# 9.2.4 查找
# 取Bob对应的值
# 1. dict[key]
# res = d['Bob']
# print(res)   # 100

# 2. dict.get(key)
# res = d.get("Bob")
# print(res)   # 100

# res = d.get("Jerry")   # get不到对应值 返回None
# print(res)   # None

# res = d.get("Bob", 1000)    # 1000默认值 如果key存在 则取出对应的值 不存在 则按默认值去走 这里默认值是1000
# print(res)
# res = d.get('Jerry', 1000)
# print(res)   # 1000

# d = {"Bob": 100, 'Alice': 20, 'Tom': 50}
# res = sorted(d.items(), key=lambda x: x[1])
# print(res)   # [('Alice', 20), ('Tom', 50), ('Bob', 100)]
#
# res = dict(res)
# print(res)   # {'Alice': 20, 'Tom': 50, 'Bob': 100}  切换回dict类型

# 10.0 Tuple 元组 (12, 32, 43, 23, '2424', [324, 24, 42]) 元组是不可变类型, 但是里面的元素如果是可变的话可以更改
a = (12, 32, 43, 23, '2424', [324, 24, 42])






























