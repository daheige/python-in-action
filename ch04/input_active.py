# 通过变量bool来控制退出程序
prompt = "enter q to end?"
active = True
# while active:
#     msg = input(prompt)
#     if msg == "q":
#         active = False
#     else:
#         print(msg)

# 通过break退出循环
while True:
    msg = input(prompt)
    if msg == "q":
        break
    else:
        print(msg)

print("program end")
