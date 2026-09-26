def this_fails():
    x = 1 / 0


try:
    this_fails()
except ZeroDivisionError as err:
    # 除以0的异常提示
    print("Handling run-time error:", err)
