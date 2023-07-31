price = 52
txt = "The price is {} dollars"
print(txt.format(price))

print("-------------------------")

# 花括号内添加参数以指定如何转换值
txt = "The price is {:.2f} dollars"
print(txt.format(price))

print("-------------------------")

# 多个值
quantity = 3
itemno = 567
price = 52
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

print("-------------------------")

# 按指定顺序
quantity = 3
itemno = 567
price = 52
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

print("-------------------------")

# 多次引用相同的值，请使用索引号
age = 63
name = "Bill"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

print("-------------------------")

# 命名参数
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Porsche", model="911"))
