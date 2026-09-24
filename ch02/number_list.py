# 创建数字列表
# range() 函数用于生成一个整数序列，不包含最后一个整数
for i in range(5):
    print("current number:", i)

# 打印1-5
for i in range(1, 6):
    print(i)

# 使⽤ range() 创建数值列表
# 使用 range(10) 生成 0 到 9 的整数序列
# 这里使用 list() 将序列转换为列表
my_list = list(range(10))

# 输出列表内容
print(my_list)

numbers = list(range(1, 6))
print(numbers)

# range还是指定步长
even_numbers = list(range(2, 11, 2))
print(even_numbers)  # [2, 4, 6, 8, 10]

s = []
for v in range(1, 11):
    s.append(v**2)  # v的2次方

print("squares:", s)  # 输出平方列表

# 对数值列表执⾏简单的统计计算
# min，max,sum函数分别用于计算最小值、最大值和总和
digits = list(range(1, 11))
print(f"min:{min(digits)}")  # 输出最小值
print(f"max:{max(digits)}")  # 输出最大值
print(f"sum:{sum(digits)}")  # 输出总和

# 列表推导式
# 列表推导式（list comprehension）
# 将 for 循环和创建新元素的代码合并成⼀⾏，并⾃动追加新元素
s = [val**2 for val in range(1, 10)]  # 生成1-9的平方列表
print(s)
