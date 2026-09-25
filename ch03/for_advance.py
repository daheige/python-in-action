# 逆向对序列进行循环，可以求出欲循环的正向序列
for i in reversed(range(1, 10, 2)):
    print(i)

# 按指定顺序循环序列，可以用 sorted() 函数，在不改动原序列的基础上，返回一个重新排序的序列
basket = ["apple", "orange", "apple", "pear", "orange", "banana"]
s = sorted(basket)
for i in s:
    print(i)

print("===sorted + set====")
# 使用 set() 去除序列中的重复元素。使用 sorted() 加 set() 则按排序后的顺序，循环遍历序列中的唯一元素
s = sorted(set(basket))
for i in s:
    print(i)
