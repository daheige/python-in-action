# 使用python标准库random
from random import choice, randint

number = randint(1, 6)
print(f"rand number is {number}")

# 在模块 random 中，另⼀个很有⽤的函数是 choice()。它将⼀个列表或
# 元组作为参数，并随机返回其中的⼀个元素
players = ["a", "b", "c", "eli"]
first_up = choice(players)  # 返回list中一个随机元素
print(first_up)
