在 Python 中，print 函数支持多种格式化打印方式，包括使用格式化字符串、f-string、以及 str.format() 方法等。以下是几种常见的格式化打印方法：

1. 使用 f-string（推荐）

f-string 是 Python 3.6 引入的格式化方式，语法简洁且性能优秀：
```python
name = "Alice"
age = 25
print(f"我的名字是 {name}，今年 {age} 岁。")
```

2. 使用 str.format() 方法

str.format() 是一种更传统的格式化方法，支持多种格式化选项：
```python
name = "Bob"
age = 30
print("我的名字是 {name}，今年 {age} 岁。".format(name=name, age=age))
```

3. 使用 % 格式化操作符

这是 Python 早期版本中常用的格式化方式，语法类似于 C 语言中的 printf：
```python
name = "Charlie"
age = 35
print("我的名字是 %s，今年 %d 岁。" % (name, age))
```


4. 格式化数字

对于数字的格式化，可以使用格式化字符串控制小数位数或显示方式：
```python
price = 123.456
print(f"价格是 ${price:.2f}")  # 输出: 价格是 $123.46
print(f"价格是 ${price:,.2f}")  # 输出: 价格是 $123.46（带千位分隔符）
```


5. 对齐和填充

可以使用格式化字符串控制输出的对齐方式和填充字符：
```python
name = "David"
print(f"{name:>10}")  # 右对齐，宽度为10
print(f"{name:<10}")  # 左对齐，宽度为10
print(f"{name:}")  # 居中对齐，宽度为10
print(f"{name:*}")  # 居中对齐，用 * 填充
```

这些方法可以满足大多数格式化打印的需求，其中 f-string 是目前推荐的方式，因为它更直观、高效且易于阅读。

# format % 转换规则
转换标记符包含两个或更多字符并具有以下组成，且必须遵循此处规定的顺序：

- '%' 字符，用于标记转换符的起始。
- 映射键（可选），由加圆括号的字符序列组成 (例如 (somename))。
- 转换旗标（可选），用于影响某些转换类型的结果。
- 最小字段宽度（可选）。 如果指定为 '*' (星号)，则实际宽度会从 values 元组的下一元素中读取，要转换的对象则为最小字段宽度和可选的精度之后的元素。
- 精度（可选），以在 '.' (点号) 之后加精度值的形式给出。 如果指定为 '*' (星号)，则实际精度会从 values 元组的下一元素中读取，要转换的对象则为精度之后的元素。
- 长度修饰符（可选）。
- 转换类型。

当右边的参数为一个字典（或其他映射类型）时，字符串中的格式 必须 包含加圆括号的映射键，对应 '%' 字符之后字典中的每一项。 映射键将从映射中选取要格式化的值。 例如：
```python
print('%(language)s has %(number)03d quote types.' %
      {'language': "Python", "number": 2})
```
https://docs.python.org/zh-cn/3.13/library/stdtypes.html#str.format

# str.format 方法用法
```python
'''
执行字符串格式化操作。 调用此方法的字符串可以包含文本字面值或者以花括号 {} 标明的替换字段。 
每个替换字段可以包含一个位置参数的数字索引，或是一个关键字参数的名称。 
返回的字符串副本中每个替换字段都会被替换为对应参数的字符串值。
'''

x = "The sum of 1 + 2 is {0}".format(1+2)
y = "The sum of {a} + {b} is {answer}".format(answer=1+2, a=1, b=2)
z = "{1} expects the {0} Inquisition!".format("Spanish", "Nobody")
print(x)
print(y)
print(z)
```

# format参考文档
http://docs.python.org/zh-cn/3.13/library/stdtypes.html#old-string-formatting
