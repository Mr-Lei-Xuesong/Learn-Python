a = 66
b = 200
if b > a:
    print("b is greater than a")

print("------------------")

a = 66
b = 66
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

print("------------------")

a = 200
b = 66
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

print("------------------")

a = 55
b = 66
print("A") if a > b else print("B")  # 这种写法还是第一次见

print("------------------")

a = 66
b = 66
print("A") if a > b else print("=") if a == b else print("B")

print("------------------")

a = 200
b = 66
c = 500
if a > b and c > a:
    print("Both conditions are True")

print("------------------")

a = 200
b = 66
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

print("------------------")

a = 66
b = 200
if b > a:
    pass
