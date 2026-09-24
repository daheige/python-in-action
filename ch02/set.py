# 集合
# 集合中的每个元素都必须是独⼀⽆⼆的
# 创建集合用花括号或 set() 函数。
# 注意，创建空集合只能用 set()，不能用 {}，{} 创建的是空字典
s1 = set()  # 创建一个空的集合
s1.add(1)
s1.add(2)
print(s1)

# 创建字面量集合
s = {"a", "b", "c"}
print(s)
if "a" in s:
    print("a in s set")

a = set("abcd")
print(a)  # {'a', 'c', 'd', 'b'}
b = set("alabcazam")
s = a - b  # 差集，存在于 a 中但不存在于 b 中的字母
print(s)

u = a | b  # 并集，a和b集合的所有元素
print(u)

s = a & b  # 交集，a和b公共部分
print(s)

# 集合也支持列表推导式
a = {x for x in "abracadabra" if x not in "abc"}
print(a)
