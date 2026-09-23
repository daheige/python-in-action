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
