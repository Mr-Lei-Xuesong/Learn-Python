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
    print(thisDict[x])
