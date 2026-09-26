import datetime as dt

now = dt.date.today()  # 今天  # noqa: DTZ011
print(now)

# 格式化输出
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

birthday = dt.date(1964, 7, 31)
age = now - birthday
print(age.days)
