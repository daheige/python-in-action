#!/usr/bin/local/bin/python3
# 指定文件编码
# -*- coding: utf-8 -*-
x = True
if x:
    print("hello,world")

print("hello")

"""
多行注释
"""

# 单行注释
m = "abc"
print(m)

m = 2
n = 1
y = m + n
print("y = ", y)

p = 17 // 3  # 向下取整除法运算会丢弃小数部分，结果为5
num = 17 % 3  # % 运算返回相除的余数
print("num = ", num)

print("17 / 3 = ", 17 / 3)  # 经典除法运算返回一个浮点数

n2 = 5**2  # 5 的平方
print("5 * 5 =", n2)

width = 20
height = 5 * 9
print("area = ", width * height)

# Python 全面支持浮点数；混合类型运算数的运算会把整数转换为浮点数
m1 = 4 * 3.75 - 1
print(m1)

# 字符串
s2 = "spam eggs"  # 单引号
s2 = "spam eggs"  # 双引号
print("s2 = ", s2)

x = "doesn't"
print(x)

# 用 print()，特殊字符会被转写，因此 \n 将产生一个新行
s = "First line.\nSecond line."  # \n 表示换行符
print(s)

# r原始字符串还有一个微妙的限制：一个原始字符串不能以奇数个 \ 字符结束；
print(r"C:\some\name")  # 请注意引号前的 r，原始字符串不转义

# 输出多行字符串
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# 3 乘以 'un'，再加 'ium'
y = 3 * "un" + "ium"
print(y)

# 相邻的两个或多个 字符串字面值 （引号标注的字符）会自动合并
# 拼接分隔开的长字符串时，这个功能特别实用
text = "Put several strings within parentheses to have them joined together."
print(text)

# 合并多个变量，或合并变量与字面值，要用 +
prefix = "Py"
print(prefix + "thon")

# 字符串支持 索引 （下标访问），第一个字符的索引是 0。单字符没有专用的类型，就是长度为一的字符串
word = "Python"
print(word[0])

# 索引还支持负数，用负数索引时，从右边开始计数：
last = word[-1]  # 最后一个字符
print(last)

# 除了索引操作，还支持 切片。 索引用来获取单个字符，而 切片 允许你获取子字符串:
# 切片索引的默认值很有用；省略开始索引时，默认值为 0，省略结束索引时，默认为到字符串的结尾
s = word[0:2]  # 从 0 号位 (含) 到 2 号位 (不含) 的字符
print(s)

# Python 字符串不能修改，是 immutable 的。因此，为字符串中某个索引位置赋值会报错

s = "supercalifragilisticexpialidocious"
n = len(s)
print(n)

# 传统的格式化打印，其效果类似于在 C 语言中使用 sprintf() 函数
# 如果 format 要求一个单独参数，则 values 可以为一个非元组对象。
# 否则的话，values 必须或者是一个包含项数与格式字符串中指定的转换符项数相同的元组，
# 或者是一个单独映射对象（例如字典）
print('%s has %d quote types.' % ('Python', 2))

# str.format 方法用法
'''
执行字符串格式化操作。 调用此方法的字符串可以包含文本字面值或者以花括号 {} 标明的替换字段。 
每个替换字段可以包含一个位置参数的数字索引，或是一个关键字参数的名称。 
返回的字符串副本中每个替换字段都会被替换为对应参数的字符串值。
'''

x = "The sum of 1 + 2 is {0}".format(1+2)
y = "The sum of {a} + {b} is {answer}".format(answer=1+2, a=1, b=2)
z = "{1} expects the {0} Inquisition!".format("Spanish", "Nobody")
print(x)
print(y)
print(z)
