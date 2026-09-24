c = True
if c:
    print("hello,world")

age = 19
if age >= 18:
    print("you are old enough to vote!")

age = 17
if age > 18:
    print("age gt 18")
else:
    print("sorry,age lt 18")

age = 12
if age < 4:
    print("age lt 4")
elif age < 18:
    print("age lt 18")
else:
    print("other")

# 检查元素是否在列表中
s = ["a", "b"]
if "a" in s:
    print("a in s")

toppings = ["m", "g", "e"]
for v in toppings:
    print(f"adding {v}")

# 判断列表是不是空
# 对于数值 0、空值 None、单引号空字符串 ''、双引号空字符串 ""、空列表 []、空元组 ()、空
# 字典 {}，Python 都会返回 False
if toppings:
    for v in toppings:
        print(f"adding {v}")
else:
    print("are you sure you want others")

a, b = 0, 1
# 斐波那契数列：
# 前两项之和即下一项的值
while a < 10:
    print(a)
    a, b = b, a + b

print("a,b=", a, b)

"""
Python 和 C 一样，任何非零整数都为真，零为假。
这个条件也可以是字符串或列表类型的值，事实上，任何序列都可以：长度非零就为真，空序列则为假。
示例中的判断只是最简单的比较。
比较操作符的写法和 C 语言一样： < （小于）、 > （大于）、 == （等于）、 <= （小于等于)、 >= （大于等于）及 != （不等于）。
"""

# print() 函数输出给定参数的值。
# 除了可以以单一的表达式作为参数（比如，前面的计算器的例子），它还能处理多个参数，包括浮点数与字符串。
# 它输出的字符串不带引号，且各参数项之间会插入一个空格，这样可以实现更好的格式化操作
a, b = 0, 1
while a < 1000:
    print(a, end=",")
    a, b = b, a + b

print("\nfinished")

# for语句
words = ["cat", "window", "defenestrate"]
for w in words:
    print(f"{w} len = {len(w)}")

# 创建一个副本
w2 = words.copy()
print(w2)

# break跳出循环
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n // x}")
            break

for num in range(2, 10):
    if num % 2 == 0:
        print(f"found an even number {num}")
        continue
    print(f"found an odd number {num}")

# 在 for 或 while 循环中 break 语句可能对应一个 else 子句。
# 如果循环在未执行 break 的情况下结束，else 子句将会执行。
# 搜索质数的 for 循环
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, "equals", x, "*", n // x)
            break
    else:
        # 循环到底未找到一个因数
        print(n, "is prime number")

# pass 占位符


# 通过def 定义函数
def http_error(status):
    # match case 模式匹配
    match status:
        case 400:
            return "Bad request"
        case 401:
            return "forbidden"
        case 404:
            return "not found"
        case 418:
            return "i'm a teapot"
        # 通过|表示或者的意思
        case 501 | 502 | 503:
            return "server inner error"
        # _表示通配符，以上都不匹配时
        case _:
            return "unknown"


s = http_error(404)
print(f"msg:{s}")

# match 可以匹配元组


# 类声明
class Point:
    # 定义初始化函数
    # self为第一个参数
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # match 模式匹配
    def where_is(p):
        match p:
            case Point(x=0, y=0):
                print("Origin")
            case Point(x=0, y=y):
                print(f"y={y}")
            case Point(x=x, y=0):
                print(f"x={x}")
            case Point():
                print("somewhere else")
            case _:
                print("not a point")


p = Point(1, 2)
p.where_is()
print(f"p.x={p.x}")
