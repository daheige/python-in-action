fd = open("./test.md", "r", encoding="utf-8")
for line in fd:
    print("current line:", line, end="")

fd.close()
