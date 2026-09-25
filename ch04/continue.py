# continue用法
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue

    print(f"current number:{n}")

x = 1
while x <= 5:
    print(x)
    x += 1

# 通过while循环移除元素
pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
while "cat" in pets:
    pets.remove("cat")

print(pets)
