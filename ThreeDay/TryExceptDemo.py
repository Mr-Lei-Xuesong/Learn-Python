# try 块将生成异常，因为 x 未定义
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

print("-------------------------")

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

print("-------------------------")

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

print("-------------------------")

# 如需抛出（引发）异常，请使用 raise 关键词
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")

print("-------------------------")

x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")
