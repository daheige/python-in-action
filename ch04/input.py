# input() 函数让程序暂停运⾏，等待⽤户输⼊⼀些⽂本。获取⽤户输⼊
# 后，Python 将其赋给⼀个变量，以便使⽤。
# 运行效果如下：
"""
python3 input.py
what is your name?daheige
your name is daheige
how old are you? 23
your age ge 18
the age 23 is odd.
enter 'q' to end program.u
enter 'q' to end program.u
u
enter 'q' to end program.q
q
"""

msg = input("what is your name?")
print(f"your name is {msg.strip()}")

# 如果转换失败就会提示错误
"""
Traceback (most recent call last):
  File "/Users/heige/web/python/python-in-action/ch04/input.py", line 8, in <module>
    age = int(age.strip())  # 将字符串转换为int数字类型
ValueError: invalid literal for int() with base 10: 'd'
"""
age = input("how old are you? ")
age = int(age.strip())  # 将字符串转换为int数字类型
if age >= 18:
    print("your age ge 18")
else:
    print("your age lt 18")

if age % 2 == 0:
    print(f"the age {age} is even.")
else:
    print(f"the age {age} is odd.")

prompt = "enter 'q' to end program."
msg = input(prompt)
while msg != "q":
    msg = input(prompt)
    print(msg)
