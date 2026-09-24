# 字符串定义，在python中，字符串可以是单引号或双引号包起来
name = "Alice"
c = "tom"
# 通过f-string格式化输出字符串
print(f"name:{name},c:{c}")

# 通过 title 方法将字符串的首字母大写

print(c.title())  # 输出 Tom

# 大小写
print(f"c 转化为大写格式{c.upper()}")  # 输出 TOM
print(f"c 转化为小写格式{c.lower()}")  # 输出 tom

# 在字符串中使⽤变量
# 要在字符串中插⼊变量的值，可先在左引号前加上字⺟ f
# 插⼊的变量放在花括号内。这样，Python 在显⽰字符串时，将把每个变量
# 都替换为其值
#
# Python f-string（格式化字符串字面量）是在 Python 3.6 引入的，对应 PEP 498
# Python 3.8 增加了 f"{x=}" 调试写法；Python 3.12 放宽了 f-string 语法限制（如同引号嵌套、多行表达式更自由等）
#
# 这种字符串称为 f 字符串。f 是 format（设置格式）的简写，因为 Python 通
# 过把花括号内的变量替换为其值来设置字符串的格式
first_name = "John"
last_name = "Doe"
full_name = f"{first_name} {last_name}"
print(full_name)  # 输出 John Doe
print(f"hello {full_name.title()}")

# 可以使⽤ f 字符串来创建消息，再把整条消息赋给变量
message = f"hello, {full_name.title()}!"
print(message)  # 输出 hello, John Doe!

# 使⽤制表符或换⾏符来添加空⽩
print("\tpython")  # 输出 python，前面有一个制表符
# 换行符
print("hello\ndaheige")

# 删除空⽩
fav = "python    "
print(f"原始字符串：{fav}")
# 使⽤ rstrip() ⽅法，删除右边的空白
print(f"删除右边的空白之后的字符串:{fav.rstrip()}")
fav1 = fav.rstrip()
print(fav1)

# 删除字符串左端的空⽩
fav2 = "    python"
v = fav2.lstrip()
print(f"删除左边的空白之后的字符串为:{v}")

fav3 = "     python   "
v = fav3.strip()
print(f"删除左右两边的空白之后的字符串为:{v}")

# 删除前缀
nostarch_url = "https://www.nostarch.com"
# 这里我去掉左边的https://
nostarch_url = nostarch_url.removeprefix("https://")
print(f"删除前缀之后的字符串为:{nostarch_url}")

file = "text.txt"
# 去掉文件名的后缀名
filename = file.removesuffix(".txt")
print(filename)
