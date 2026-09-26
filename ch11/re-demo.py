import re

# 正则查找
s = re.findall(r"\bf[a-z]*", "which foot or hand fell fastest")
print(s)
s1 = re.sub(r"(\b[a-z]+) \1", r"\1", "cat in the the hat")
print(s1)

s = "tea for too".replace("too", "two")
print(s)
