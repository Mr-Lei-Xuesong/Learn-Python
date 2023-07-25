# 创建集合
thisSet = {"apple", "banana", "cherry"}
print(thisSet)

print("------------------")

# 访问项目
thisSet = {"apple", "banana", "cherry"}
for x in thisSet:
    print(x)

print("------------------")

# 检查项目是否存在
thisSet = {"apple", "banana", "cherry"}
print("banana" in thisSet)

print("------------------")

# 更改项目:一旦创建了集合，您就无法更改其项目原有内容，但是可以添加新项目
thisSet = {"apple", "banana", "cherry"}
thisSet.add("orange")
print(thisSet)

print("------------------")

# 添加多个项目
thisSet = {"apple", "banana", "cherry"}
thisSet.update(["orange", "mango", "grapes"])
print(thisSet)

print("------------------")

# 获取集合长度
thisSet = {"apple", "banana", "cherry"}
print(len(thisSet))

print("------------------")

# 删除项目
thisSet = {"apple", "banana", "cherry"}
thisSet.remove("banana")
print(thisSet)

print("------------------")

# remove删除项目,如果项目不存在，则删除会引发错误
thisSet = {"apple", "banana", "cherry"}
thisSet.discard("banana")
print(thisSet)

print("------------------")

# 删除最后一个项目
thisSet = {"apple", "banana", "cherry"}
x = thisSet.pop()  # set 是无序的，因此您不会知道被删除的是什么项目
print(x)
print(thisSet)

print("------------------")

# 清空集合
thisSet = {"apple", "banana", "cherry"}
thisSet.clear()
print(thisSet)

print("------------------")

# 删除集合
thisSet = {"apple", "banana", "cherry"}
del thisSet

print("------------------")

# 合并两个集合:union() 方法返回一个新集合，其中包含两个集合中的所有项目
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

print("------------------")

# update() 方法将集合的项目插入当前集合
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

print("------------------")

# 插入此集合和另一个集合的对称差集
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)

print("------------------")

# 返回具有两组集合的对称差集的集合
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

print("------------------")

# 返回此集合是否包含另一个集合
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print(set1.isdisjoint(set2))

print("------------------")

# 返回另一个集合是否包含此集合
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print(set1.issubset(set2))

print("------------------")

# 返回两个集合是否有交集
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print(set1.isdisjoint(set2))

print("------------------")

# 删除此集合中不存在于其他指定集合中的项目
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)

print("------------------")

# 返回为两个其他集合的交集的集合
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)
