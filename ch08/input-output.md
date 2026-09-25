# 输入和输出

## 输出格式化
- 使用 格式化字符串字面值 ，要在字符串开头的引号/三引号前添加 f 或 F 。在这种字符串中，可以在 { 和 } 字符之间输入引用的变量，或字面值的 Python 表达式。
- 字符串的 str.format() 方法需要更多手动操作。 你仍将使用 { 和 } 来标记变量将被替换的位置并且可以提供详细的格式化指令，但你还需要提供待格式化的信息。 
```python
yes_votes = 42_572_654
total_votes = 85_705_149
percentage = yes_votes / total_votes
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)) # 42572654 YES votes  49.67%
```

如果不需要花哨的输出，只想快速显示变量进行调试，可以用 repr() 或 str() 函数把值转化为字符串。

str() 函数返回供人阅读的值，repr() 则生成适于解释器读取的值 (如果没有等效的语法，则强制引发 SyntaxError)。对于没有支持供人阅读展示结果的对象， str() 返回与 repr() 相同的值。 一般情况下，数字、列表或字典等结构的值，使用这两个函数输出的表现形式是一样的。 字符串有两种不同的表现形式

```python
s = 'Hello, world.'
str(s)

repr(s)

str(1/7)

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)

# 字符串的 repr() 会添加引号和反斜杠：
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)

# repr() 的参数可以是任何 Python 对象：
repr((x, y, ('spam', 'eggs')))
```
