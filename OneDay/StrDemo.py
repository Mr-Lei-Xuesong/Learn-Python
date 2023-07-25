a = "Hello"
print(a)

print("------------------")

a = """Python is a widely used general-purpose, high level programming language. 
It was initially designed by Guido van Rossum in 1991 
and developed by Python Software Foundation. 
It was mainly developed for emphasis on code readability, 
and its syntax allows programmers to express concepts in fewer lines of code."""
print(a)

print("------------------")

a = '''Python is a widely used general-purpose, high level programming language. 
It was initially designed by Guido van Rossum in 1991 
and developed by Python Software Foundation. 
It was mainly developed for emphasis on code readability, 
and its syntax allows programmers to express concepts in fewer lines of code.'''
print(a)

print("------------------")

a = "Hello, World!"
print(a[1])

print("------------------")

b = "Hello, World!"
print(b[2:5])

print("------------------")

# strip() 方法删除开头和结尾的空白字符
a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"

print("------------------")

# 字符串长度
a = "Hello, World!"
print(len(a))

print("------------------")

# lower() 方法返回字符串中所有大写字符转换为小写
a = "Hello, World!"
print(a.lower())

print("------------------")

# upper() 方法返回字符串中所有小写字符转换为大写
a = "Hello, World!"
print(a.upper())

print("------------------")

# replace() 方法替换字符串中的某个字符
a = "Hello, World!"
print(a.replace("H", "J"))

print("------------------")

# split() 方法分割字符串，返回分割后的字符串列表
a = "Hello, World!"
print(a.split(","))  # returns ['Hello', ' World!']

print("------------------")

# 检查字符串是否以指定的字符开头
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

print("------------------")

# 检查字符串是否以指定的字符结尾
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

print("------------------")

# 检查字符串
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

print("------------------")

# 字符串格式
age = 63
txt = "My name is Bill, and I am {}"
print(txt.format(age))

quantity = 3
itemNo = 567
price = 49.95
myOrder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myOrder.format(quantity, itemNo, price))

# 字符串格式化
# 1. %s 格式化字符串
# 2. %d 格式化整数
# 3. %f 格式化浮点数
# 4. %.<number of digits>f 格式化浮点数，指定小数点后的精度
# 5. %x 格式化十六进制数
# 6. % 格式化字符串

print("------------------")

# 可用于确定对象是否具有某种数据类型
x = 200
print(isinstance(x, int))
