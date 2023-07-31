import datetime

# 获取当前时间
now = datetime.datetime.now()
print(now)

print(now.strftime("%Y-%m-%d %H:%M:%S"))

print(now.strftime("%a, %b %d %H:%M"))

print(now.strftime("%Y%m%d"))

print(now.strftime("%H:%M:%S"))

print(now.year)
print(now.month)
print(now.day)
print(now.strftime("%A"))

print("--------------------")

# 创建一个指定日期的时间
dt = datetime.datetime(2019, 12, 31, 23, 59, 59)
print(dt)
