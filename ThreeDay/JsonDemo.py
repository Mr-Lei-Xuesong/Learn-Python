import json

# some JSON:
x = '{ "name":"Bill", "age":63, "city":"Seatle"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])

print("----------------------------------")

# Python 对象（字典）：
x = {
    "name": "Bill",
    "age": 63,
    "city": "Seatle"
}

# 转换为 JSON：
y = json.dumps(x)

# 结果是 JSON 字符串：
print(y)

print("----------------------------------")

print(json.dumps({"name": "Bill", "age": 63}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

print("----------------------------------")

x = {
    "name": "Bill",
    "age": 63,
    "married": True,
    "divorced": False,
    "children": ("Jennifer", "Rory", "Phoebe"),
    "pets": None,
    "cars": [
        {"model": "Porsche", "mpg": 38.2},
        {"model": "BMW M5", "mpg": 26.9}
    ]
}

print(json.dumps(x, indent=4))  # 使用 indent 参数定义缩进数量

print("----------------------------------")

json.dumps(x, indent=4, sort_keys=True)  # 使用 sort_keys 参数来指定是否排序
