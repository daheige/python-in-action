import random

print(random.choice(["a", "b", "c"]))  # 随机返回列表中的一个元素

s = random.sample(range(100), 10)  # 随机返回10个100之内的数字
print(s)

# 返回[0.0,1.0] 区间的随机浮点数
f = random.random()
print(f)

# 从range(6) 返回0-5之间的数字
# random.randrange(6) 等价于 random.randrange(0, 6)，
# 返回 [0, 5] 之间的整数（含 0 和 5）
number = random.randrange(6)
print(number)

print(random.randint(0, 6))  # 0~6，可能返回 6！
print(random.randrange(0, 6))  # 0~5，绝不会返回 6
