# 创建元组
thisTuple = ("apple", "banana", "cherry")
print(thisTuple)

print("------------------")

# 访问元组项目
thisTuple = ("apple", "banana", "cherry")
print(thisTuple[1])

thisTuple = ("apple", "banana", "cherry")
print(thisTuple[-1])

thisTuple = ("apple", "banana", "cherry")
print(thisTuple[1:3])

thisTuple = ("apple", "banana", "cherry")
print(thisTuple[-3:-1])

print("------------------")

# 更改元组值,创建元组后，您将无法更改其值。元组是不可变的，或者也称为恒定的
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

print("------------------")

# 循环元组
thisTuple = ("apple", "banana", "cherry")
for x in thisTuple:
    print(x)

print("------------------")

# 检查项目是否存在
thisTuple = ("apple", "banana", "cherry")
if "apple" in thisTuple:
    print("Yes, 'apple' is in the fruits tuple")

print("------------------")

# 元组长度
thisTuple = ("apple", "banana", "cherry")
print(len(thisTuple))

print("------------------")

# 创建有一个项目的元组
thisTuple = ("apple",)  # 如需创建仅包含一个项目的元组，您必须在该项目后添加一个逗号，否则 Python 无法将变量识别为元组
print(type(thisTuple))

print("------------------")

# 删除元组,元组是不可更改的，因此您无法从中删除项目，但您可以完全删除元组
thisTuple = ("apple", "banana", "cherry")
del thisTuple

print("------------------")

# 合并两个元组
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# tuple() 构造函数
thisTuple = tuple(("apple", "banana", "cherry"))  # 注意双括号
print(thisTuple)

print("------------------")

# 返回元组中指定值出现的次数
thisTuple = (1, 2, 3, 4, 5, 1, 1)
x = thisTuple.count(1)
print(x)

print("------------------")
# 在元组中搜索指定的值并返回它被找到的位置
thisTuple = (1, 2, 3, 4, 5, 1, 1)
x = thisTuple.index(5)
print(x)

print("------------------")
# 使用 tuple() 方法来创建元组
thisTuple = tuple(("apple", "banana", "cherry"))  # 请注意双括号
print(thisTuple)
