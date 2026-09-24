message = "Hello, World!"
print(message)

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
