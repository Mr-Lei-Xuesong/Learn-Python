# 创建字典
thisDict = {
    "brand": "Porsche",
    "model": "911",
    "year": 1963
}
print(thisDict)

print("------------------")

# 访问字典项目
x = thisDict["model"]
print(x)

print("------------------")
x = thisDict.get("year")
print(x)

print("------------------")

# 更改字典项目
thisDict["year"] = 2018
print(thisDict)

print("------------------")

# 循环字典,逐个打印字典中的所有键名
for x in thisDict:
    print(x)

print("------------------")

# 逐个打印字典中的所有键值
for x in thisDict:
    print("key:", x, "value:", thisDict.get(x))

print("------------------")

# 使用 values() 函数返回字典的值
for x in thisDict.values():
    print(x)

print("------------------")

# 使用 items() 函数返回字典的键值对
for x, y in thisDict.items():
    print(x, y)

print("------------------")

# 检查键是否存在
if "model" in thisDict:
    print("Yes, 'model' is one of the keys in the thisDict dictionary")

print("------------------")

# 字典长度
print(len(thisDict))

print("------------------")

# 添加项目
thisDict["color"] = "red"
print(thisDict)

print("------------------")

# 删除项目,pop() 方法删除具有指定键名的项
thisDict.pop("model")
print(thisDict)

print("------------------")

# popitem() 方法删除最后插入的项,在 3.7 之前的版本中，删除随机项目
thisDict.popitem()
print(thisDict)

print("------------------")

# del 关键字删除指定的项
del thisDict["brand"]
print(thisDict)

print("------------------")

# del 关键字删除整个字典
del thisDict

print("------------------")

# clear() 方法清空字典
thisDict = {
    "brand": "Porsche",
    "model": "911",
    "year": 1963
}
thisDict.clear()
print(thisDict)

print("------------------")

# 复制字典
thisDict = {
    "brand": "Porsche",
    "model": "911",
    "year": 1963
}
myDict = thisDict.copy()
print(myDict)

print("------------------")

# 嵌套字典
myFamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(myFamily)

print("------------------")

# 创建三个字典，然后创建一个包含其他三个字典的字典
child1 = {
    "name": "Phoebe Adele",
    "year": 2002
}
child2 = {
    "name": "Jennifer Katharine",
    "year": 1996
}
child3 = {
    "name": "Rory John",
    "year": 1999
}

myFamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

print(myFamily)
