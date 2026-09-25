# try-except语句
try:
    print(5 / 0)
except ZeroDivisionError:
    # 异常处理逻辑
    print("divide invalid")

number = input("input number:")
try:
    num = int(number)
except:  # noqa: E722
    print("invalid number")
else:
    print(num)
