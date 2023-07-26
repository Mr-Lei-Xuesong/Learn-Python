def my_function():
    print("Hello from a function")


my_function()

print("-------------------")


def my_function(name):
    print(name + " Gates")


my_function("Bill")
my_function("Steve")
my_function("Elon")

print("-------------------")


def my_function(country="China"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

print("-------------------")


def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)

print("-------------------")


def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))

print("-------------------")


def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Phoebe", child2="Jennifer", child3="Rory")

print("-------------------")


def my_function(*kids):
    print("The youngest child is " + kids[1])


my_function("Phoebe", "Jennifer", "Rory")

print("-------------------")


def myfunction():
    pass


print("-------------------")


def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("Recursion Example Results")
tri_recursion(6)
