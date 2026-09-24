# list 列表
列表（list）由⼀系列按特定顺序排列的元素组成。你不仅可以创建包含字⺟表中所有字⺟、数字 0〜9 或所有家庭成员姓名的列表，还可以将任何东⻄加⼊列表，其中的元素之间可以没有任何关系。列表通常包含多个元素，因此给列表指定⼀个表⽰复数的名称（如 letters、digits 或 names）是个不错的主意。

在 Python 中，⽤⽅括号（[]）表⽰列表，⽤逗号分隔其中的元素

```python
bicycles = ["trek","cannondale","redline"]
print(bicycles)
```

# del 和 pop 选择
如果要从列表中删除⼀个元素，且不再以任何⽅式使⽤它，就使⽤ del 语句；如果要在删除元素后继续使⽤它，就使⽤ pop() ⽅法。

# list 基本操作
```python
squares = [1, 4, 9, 16, 25]
print("squares:", squares)

# 和字符串（及其他内置 sequence 类型）一样，列表也支持索引和切片
last = squares[-1]
print(last)

n = squares[-3:]  # 切片操作将返回一个新列表
print("n:", n)

# 列表是 mutable 类型，其内容可以改变
squares[3] = 64
print("squares:", squares)

# 可以通过使用 list.append() 方法，在列表末尾添加新条目
# list.append() takes exactly one argument
squares.append(1)
print("squares:", squares)

# Python 中的简单赋值绝不会复制数据。 当你将一个列表赋值给一个变量时，该变量将引用 现有的列表。
# 你通过一个变量对列表所做的任何更改都会被引用它的所有其他变量看到
rgb = ["Red", "Green", "Blue"]
rgba = rgb
b = id(rgb) == id(rgba)  # 它们指向同一个对象
print(b)
rgba.append("Alph")
print("rgba", rgba)
print("rgb", rgb)

# 切片操作返回包含请求元素的新列表。以下切片操作会返回列表的 浅拷贝
correct_rgba = rgba[:]  # 浅拷贝，不会改变原有的切片rgba
correct_rgba[-1] = "Alpha"
print("correct_rgba", correct_rgba)
print("rgba", rgba)
letters = ["a", "b", "c", "d", "e", "f", "g"]

# 改变切片大小
print("letters", letters)
# ["a", "b", "c", "d", "e", "f", "g"]
letters[2:5] = ["C", "D", "E"]
letters[2:5] = []  # 这里是清空下标从2-5元素的值
print("letters", letters)

letters = ["a", "b", "c", "d"]
print("letters.len=", len(letters))

# 通过用一个空列表替代所有元素来清空列表
letters[:] = []
print("letters", letters)
```

# 索引不存在的错误
```ini
motorcycles = ['honda', 'yamaha', 'suzuki']
>>> motorcycles[4]
Traceback (most recent call last):
  File "<python-input-8>", line 1, in <module>
    motorcycles[4]
    ~~~~~~~~~~~^^^
IndexError: list index out of range
>>>
```
