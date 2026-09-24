players = ["c", "m", "chael", "eli"]
print(players)

# 获取0-3位置的切片
s = players[0:3]
print(s)

# 索引下标是从0开始的，不包含终止位置的索引元素
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[1:4])

# 如果没有指定第⼀个索引，Python 将⾃动从列表开头开始
print(players[:4])  # 表示从0到3索引位置的元素

# 提取从第三个元素到末尾
print(players[2:])

# 提取末尾最后3个元素
s = players[-3:]
print(s)

# 要复制列表，可以创建⼀个包含整个列表的切⽚，⽅法是同时省略起始索
# 引和终⽌索引（[:]）
s2 = players[:]
print(s2)

# 小心原有元素被修改
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods
friend_foods.append("li")  # 对切片追加元素后，发现原来的list也发生了变化
print("my_foods:", my_foods)
print("friend_foods:", friend_foods)
"""
这⾥将 my_foods 赋给 friend_foods，⽽不是将 my_foods 的副本赋
给 friend_foods。这种语法实际上是让 Python 将新变量
friend_foods 关联到已与 my_foods 相关联的列表，因此这两个变量指
向同⼀个列表。
"""
