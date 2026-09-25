# while 和 input组合使用
"""
python3 mountain_poll.py

your name?daheige
your fav?go
Would you like to let another person respond?(yes/no)yes

your name?alex
your fav?rust
Would you like to let another person respond?(yes/no)yes

your name?rob
your fav?go
Would you like to let another person respond?(yes/no)no
poll res: {'daheige': 'go', 'alex': 'rust', 'rob': 'go'}
daheige like:go
alex like:rust
rob like:go
"""

res = {}
active = True

while active:
    name = input("\nyour name?")
    fav = input("your fav?")
    res[name] = fav

    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat == "no":
        active = False

print("poll res:", res)
for name, val in res.items():
    print(f"{name} like:{val}")
