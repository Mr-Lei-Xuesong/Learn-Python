class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)

print("--------------------")


class Person:
    def __init__(self, name, age):  # 构造函数，每次使用类创建新对象时，都会自动调用 __init__() 函数
        self.name = name
        self.age = age


p1 = Person("John", 36)
print(p1.name)
print(p1.age)

print("--------------------")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFunc(self):
        print("Hello my name is " + self.name)  # self 参数是对类的当前实例的引用，用于访问属于该类的变量


p1 = Person("Bill", 63)
p1.myFunc()
p1.name = "Tom"
p1.myFunc()
del p1.age  # 删除对象的属性
# print(p1.age)  # 删除对象的属性后，再次访问该属性会报错
del p1  # 删除对象
# print(p1)  # 删除对象后，再次访问该对象会报错
print("--------------------")


class Person:
    pass  # 空类
