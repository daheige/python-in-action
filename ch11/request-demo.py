from urllib.request import urlopen

# 发送请求
# 输出 Last updated on Sep 26, 2026 (02:42 UTC).
with urlopen("https://docs.python.org/3/") as response:
    for line in response:
        line = line.decode()
        if "updated" in line:
            print(line.rstrip())
