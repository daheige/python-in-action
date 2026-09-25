# 字典map数据结构
# 类似其他语言的hash 哈希数据结构
h = {
    "a": 1,
    "b": 2,
}
print(h)

print(h["a"])

print(h.get("a"))
# 可使⽤ get() ⽅法在指定的键不存在时返回⼀个默认值
# get() ⽅法的第⼀个参数⽤于指定键，是必不可少的；第⼆个参数为当指定的键不
# 存在时要返回的值，是可选的
print(h.get("c", "no value"))  # no value输出默认值

# 给map添加新的key/val
h["c"] = 1
print(h)

print("a in h:", "a" in h)

# 删除map中的元素
del h["a"]
print(h)

# 通过list函数获取所有的keys
keys = list(h)
print(keys)

keys = sorted(h)
print(keys)
print(h)

# dict() 构造函数可以直接用键值对序列创建字典
h = dict([("a", 1), ("b", 2)])
print(h)

# 字典推导式可以用任意键值表达式创建字典
h = {x: x**2 for x in (2, 4, 6)}
print(h)  # {2: 4, 4: 16, 6: 36}

# 直接通过关键字参数指定key声明map
h = dict(sape=4139, guido=4127, jack=4098)
print(h)

# 创建一个空的字典
h = {}
h["color"] = "green"
h["points"] = 3
print(h)
h["color"] = "yellow"  # 直接修改即可
print(h)

# 遍历字典中的所有键
# 如果显式地使⽤ keys() ⽅法能让代码更容易理解，就可以选择这样做，
# 但如果你愿意，也可以省略它，直接用 for key in h
for key in h.keys():  # noqa: SIM118
    print(key)

# 按照特定顺序遍历map
for key in sorted(h.keys()):
    print(f"key:{key.title()}")

# 遍历字典中的所有值
for value in h.values():
    print("value:", value)

# 循环的技巧
# 循环map
# 对字典执行循环时，可以使用 items() 方法同时提取键及其对应的值
knights = {"gallahad": "the pure", "robin": "the brave"}
for k, v in knights.items():
    print(k, v)

# 对于序列循环时候，可以用 enumerate() 函数可以同时取出位置索引和对应的值
s = ["tic", "tac", "toe"]
for index, val in enumerate(s):
    print(index, val)

# 同时循环两个或多个序列时，用 zip() 函数可以将其内的元素一一匹配
questions = ["name", "quest", "favorite color"]
answers = ["lancelot", "the holy grail", "blue"]
for q, a in zip(questions, answers):
    print(f"what is your {q}? it is {a}")
