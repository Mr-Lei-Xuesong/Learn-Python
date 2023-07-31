class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


# 使用 Person 来创建对象，然后执行 printname 方法：
x = Person("Bill", "Gates")
x.printname()

print("----------子类----------")


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)  # super() 函数是用于调用父类(超类)的一个方法
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


x = Student("Elon", "Musk", 2019)
x.printname()
x.welcome()
