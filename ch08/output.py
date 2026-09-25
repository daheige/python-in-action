import math

year = 2026
event = "referrendum"
print(f"result of the {year} {event}")

year_votes = 123_090_890
total_votes = 87_908_980
percentage = year_votes / total_votes
print(f"{year_votes:-9} yes votes {percentage:2.2%}")

s = "Hello, world."
print(str(s))

print(repr(s))  # 'Hello, world.'
print(str(1 / 7))

x = 10 * 3.25
y = 200 * 200
s = "The value of x is " + repr(x) + ", and y is " + repr(y) + "..."
print(s)
# 字符串的 repr() 会添加引号和反斜杠：
hello = "hello, world\n"
hellos = repr(hello)  # 'hello, world\n'
print(hellos)

# repr() 的参数可以是任何 Python 对象
print(repr((x, y, ("m", "n"))))

# 格式化字符串字面值 （简称为 f-字符串）在字符串前加前缀 f 或 F，通过 {expression} 表达式，把 Python 表达式的值添加到字符串内。
# 在 ':' 后传递整数，为该字段设置最小字符宽度，常用于列对齐
print(f"pi is {math.pi:.3f}")  # pi is 3.142

table = {"Sjoerd": 4127, "Jack": 4098, "Dcab": 7678}
for name, phone in table.items():
    print(f"{name:10} ==> {phone:10d}")

# = 说明符可被用于将一个表达式扩展为表达式文本、等号再加表达式求值结果的形式。
bugs = "roaches"
count = 13
area = "living room"
# Debug bugs='roaches' count=13 area='living room'
print(f"Debug {bugs=} {count=} {area=}")

# str.format() 方法 格式化输出
# 此时 format 中的占位符参数是一个多个任意参数，作为前面占位符对应的值
print('We are the {} who say "{}!"'.format("knights", "Ni"))

# 花括号及之内的字符（称为格式字段）被替换为传递给 str.format() 方法的对象
print("{0} and {1}".format("span", "egg"))  # span and egg

# str.format() 方法中使用关键字参数名引用值
print("this {food} is {adjective}".format(food="span", adjective="horrible"))

# 位置参数和关键字参数可以任意组合
print("The story of {0}, {1}, and {other}.".format("Bill", "Manfred", other="Georg"))

# 如果不想分拆较长的格式字符串，最好按名称引用变量进行格式化，不要按位置。
# 这项操作可以通过传递字典，并用方括号 '[]' 访问键来完成。
table = {"Sjoerd": 4127, "Jack": 4098, "Dcab": 8637678}
print(f"Jack: {table['Jack']:d}; Sjoerd: {table['Sjoerd']:d}; Dcab: {table['Dcab']:d}")

# 通过将 table 字典作为采用 ** 标记的关键字参数传入来实现
table = {"Sjoerd": 4127, "Jack": 4098, "Dcab": 8637678}
print("Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}".format(**table))

# 对齐
for x in range(1, 11):
    print(f"{x:2d} {x * x:3d} {x * x * x:4d}")

# str.zfill() ，该方法在数字字符串左边填充零，且能识别正负号
print("12".zfill(5))
print("-3.14".zfill(7))
print("3.14159265359".zfill(5))

# % 运算符 (求余) 也可被用于字符串格式化。 给定 format % values (其中 format 是一个字符串)，
# 则 format 中的 % 转换占位符将以 values 中的零个或多个元素来替换。 此操作通常称为字符串插值。
print("The value of pi is approximately %5.3f." % math.pi)
