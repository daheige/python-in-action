bicycles = ["trek", "cannondale", "redline"]  # 定义列表
print("bicycles:", bicycles)

# 访问列表元素
# 列表是有序集合，因此要访问列表的任何元素，只需要将该元素的位置，索引告诉python即可
# 索引从 0 ⽽不是 1 开始
print("bicycles[0]:", bicycles[0])  # 输出列表的第一个元素
print("bicycles[1]:", bicycles[1])  # 输出列表的第二个元素
print("bicycles[2]:", bicycles[2])  # 输出列表

print(f"trek title:{bicycles[0].title()}")  # 输出 Trek

# 访问最后⼀个列表元素
print("last bicycle:", bicycles[-1])

print(bicycles[-2])  # 输出列表的倒数第二个元素
print(bicycles[-3])  # 输出列表的倒数第三个元素

# 修改列表元素
bicycles[0] = "giant"
print("bicycles:", bicycles)

# 追加元素
bicycles.append("ducati")
print("bicycles:", bicycles)

# 在列表中插⼊元素，这里的insert表示在某个index位置插入元素，原来的元素会向后移动
bicycles.insert(0, "harley")
print("bicycles:", bicycles)

# 从列表中删除元素，使用关键字del，del语句删除列表元素时，Python不会返回被删除的值。
# 它只是从列表中删除该元素，并且该元素不再存在
# 使⽤ del 可删除任意位置的列表元素，只需要知道其索引即可
del bicycles[0]
print("new bicycles:", bicycles)

# 使⽤ pop() ⽅法删除元素
# pop() ⽅法删除列表末尾的元素，并让你能够接着使⽤它。术语弹出
# （pop）源⾃这样的类⽐：列表就像⼀个栈，⽽删除列表末尾的元素相
# 当于弹出栈顶元素。
last = bicycles.pop()  # 删除列表末尾的元素，并返回该元素
print(f"last bicycle:{last}")
print("new bicycles:", bicycles)

# 删除列表中任意位置的元素，传入对应的index索引即可
bicycles.pop(0)  # 删除列表中第一个元素
print("new bicycles:", bicycles)

# 根据值删除元素
# remove() ⽅法只删除第⼀个指定的值。如果要删除的值
# 可能在列表中出现多次，就需要使⽤循环，确保将每个值都删除
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
motorcycles.remove("honda")
print("new motorcycles:", motorcycles)

# sort对列表进行排序
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()  # 按字母顺序排序
print("cars:", cars)

# 对列表按相反顺序排序
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort(reverse=True)  # 反向排序
print("cars:", cars)

# 使⽤ sorted() 函数对列表进⾏临时排序，不影响原来的列表顺序
cars = ["bmw", "audi", "toyota", "subaru"]
c2 = sorted(cars)
print("cars:", cars)
print("c2:", c2)
c3 = sorted(cars, reverse=True)
print("c3:", c3)

# 反向打印列表
cars = ["bmw", "audi", "toyota", "subaru"]
cars.reverse()  # 反向打印列表
print("reverse cars:", cars)
print("len cars:", len(cars))
