d = (12, 100)
# 元组的元素是 immutable （不可变的）
# d[0] = 1 # TypeError: 'tuple' object does not support item assignment
print(d)

"""
严格地说，元组是由逗号标识的，圆括号只是让元组看起来更
整洁、更清晰。如果你要定义只包含⼀个元素的元组，必须在这个元
素后⾯加上逗号：
"""
my_t = (1,)
print(my_t)

# 遍历元组中的所有值
for item in d:
    print(f"current item:{item}")

# 修改整个元组
my_t = (1, 2, 3)
for item in my_t:
    print(f"current item:{item}")
