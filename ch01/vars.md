# 变量命名方式
1. 类名：大驼峰命名
```python
class MyClass
    pass
```
2. 常量：大写蛇形命名方式
```python
MAX_SIZE = 100
```
3. 变量，函数：小写蛇形命名方式
```python
user_name = "daheige"
def my_fnc():
    pass
```

完整demo如下：
```python
cat = "tom"
print(f"cat:{cat}")

name = "Alice"
age = 25
# 格式化输出
print(f"我的名字是 {name}，今年 {age} 岁。")

# 常量命名，大写蛇形命名方式
MAX_SIZE = 100
print(f"最大尺寸为 {MAX_SIZE}")

user_name = "daheige"
print(f"用户名是 {user_name}")


# 函数定义
def say_hello(name: str) -> str:
    return f"Hello, {name}!"


print(say_hello("Alice"))
```

# 小结
- 变量名只能包含字⺟、数字和下划线1。变量名能以字⺟或下划线打头，但不能以数字打头。例如，可将变量命名为 message_1，但不能将其命名为 1_message。
- 变量名不能包含空格，但能使⽤下划线来分隔其中的单词。例如，变量名 greeting_message 可⾏，但变量名 greeting message 会引发错误。
- 不要将 Python 关键字和函数名⽤作变量名。例如，不要将 print ⽤作变量名，因为它被 Python 留作特殊⽤途。
- 变量名应既简短⼜具有描述性。例如，name ⽐ n 好，student_name ⽐ s_n 好，name_length ⽐length_of_persons_name 好。慎⽤⼩写字⺟ l 和⼤写字⺟ O，因为它们可能被⼈错看成数字 1 和 0。
