# 遍历列表，使用for in 语句遍历元素
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician)  # 输出列表中的每个元素

# 在for循环中使用元素
for magician in magicians:
    # 输出列表中的每个元素，并格式化输出
    print(f"{magician.title()}, that was a great trick!")

# Python 根据缩进来判断代码⾏与程序其他部分的关系
# 下面的代码没有正常缩紧，运行错误
"""
message = "Hello Python world!"
 print(message)

运行错误
File "/Users/heige/web/python/python-in-action/ch02/list_for_in.py", line 14
    print(message)
IndentationError: unexpected indent
"""
