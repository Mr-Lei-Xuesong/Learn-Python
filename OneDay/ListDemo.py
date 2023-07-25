# 通过引用索引号来访问列表项
thisList = ["apple", "banana", "cherry"]
print(thisList[1])

print("------------------")

# 通过负数索引号来访问列表项
thisList = ["apple", "banana", "cherry"]
print(thisList[-1])

print("------------------")

# 通过范围索引号来访问列表项
thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thisList[2:5])  # 从索引 2（包括）开始，到索引 5（不包括）结束

print("------------------")

# 更改项目值
thisList = ["apple", "banana", "cherry"]
thisList[1] = "blackcurrant"
print(thisList)

print("------------------")

# 循环列表
thisList = ["apple", "banana", "cherry"]
for x in thisList:
    print(x)

print("------------------")

# 检查项目是否存在
thisList = ["apple", "banana", "cherry"]
if "apple" in thisList:
    print("Yes, 'apple' is in the fruits list")

print("------------------")

# 列表长度
thisList = ["apple", "banana", "cherry"]
print(len(thisList))

print("------------------")

# 添加项目
thisList = ["apple", "banana", "cherry"]
thisList.append("orange")
print(thisList)

print("------------------")

# 插入项目
thisList = ["apple", "banana", "cherry"]
thisList.insert(1, "orange")
print(thisList)

print("------------------")

# 删除项目
thisList = ["apple", "banana", "cherry"]
thisList.remove("banana")
print(thisList)

print("------------------")

# pop() 方法删除指定的索引（如果未指定索引，则删除最后一项）
thisList = ["apple", "banana", "cherry"]
thisList.pop()
print(thisList)

print("------------------")

# del 关键字删除指定的索引
thisList = ["apple", "banana", "cherry"]
del thisList[0]
print(thisList)

# del 关键字也能完整地删除列表
thisList = ["apple", "banana", "cherry"]
del thisList

# clear() 方法清空列表
thisList = ["apple", "banana", "cherry"]
thisList.clear()
print(thisList)

print("------------------")

# 复制列表
thisList = ["apple", "banana", "cherry"]
myList = thisList.copy()
print(myList)

print("------------------")

# list() 方法复制列表
thisList = ["apple", "banana", "cherry"]
mylist = list(thisList)
print(mylist)

print("------------------")

# 合并两个列表
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

print("------------------")

# 使用 for 循环来创建列表
thisList = []
for i in range(5):
    thisList.append(i)
print(thisList)

print("------------------")
# 使用 extend() 方法将 list2 添加到 list1 的末尾
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

print("------------------")
thisList = list(("apple", "banana", "cherry"))  # 请注意双括号
print(thisList)
