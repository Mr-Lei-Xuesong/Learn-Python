import re

txt = "China is a great country"
x = re.search("^China.*country$", txt)  # 以 China 开头，country 结尾
print(x)

print("----------------------------------")

# findall() 函数返回包含所有匹配项的列表
str = "China is a great country"
x = re.findall("a", str)
print(x)

print("----------------------------------")

# search() 函数返回一个匹配的对象，如果有多个匹配，则返回第一个匹配的对象
str = "China is a great country"
x = re.search("\s", str)

print("The first white-space character is located in position:", x.start())

print("----------------------------------")

# split() 函数返回一个列表，列表元素是字符串的拆分结果
str = "China is a great country"
x = re.split("\s", str)
print(x)

print("----------------------------------")

# 通过指定 maxsplit 参数来控制出现次数
str = "China is a great country"
x = re.split("\s", str, 1)
print(x)

print("----------------------------------")

# sub() 函数替换字符串中的每个匹配项
str = "China is a great country"
x = re.sub("\s", "9", str)
print(x)

print("----------------------------------")

# 通过指定 count 参数来控制替换次数
str = "China is a great country"
x = re.sub("\s", "9", str, 2)
print(x)

print("----------------------------------")

# Match 对象是包含匹配结果的对象
str = "China is a great country"
x = re.search(r"\bC\w+", str)
print(x)  # 这将输出匹配的对象,如果没有匹配项，则返回值 None，而不是 Match 对象
print(x.span())  # 返回的元组包含了匹配的开始和结束位置
print(x.string)  # 返回传入函数的字符串
print(x.group())  # 返回匹配的字符串
