def greet():
    print("This is a test function.")
    print("Done with function call.")


print('\n##############################')


def add(a, b):
    print("Addition of numbers is:", a + b)


def multiply(a, b):
    print("Multiplication of numbers is:", a * b)


def mod(a, b):
    print("Mod of numbers is:", a % b)
    return a % b


def add_sub(a, b):
    print("Addition of numbers is:", a + b)
    print("Subtraction of numbers is:", a - b)
    return a + b, a - b


greet()
add(2, 3)
multiply(4, 5)
result = mod(20, 3)
print("Mod of numbers is:", result)

print('\n##############################')

result1, result2 = add_sub(20, 3)
print("Addition of numbers is:", result1)
print("Subtraction of numbers is:", result2)

print('\n############PASS BY VALUE/REFERENCE - NOT IN PYTHON##################')


def update(x):
    print(id(x))
    x = 8
    print(id(x))
    print("Value inside function is", x)


update(10)

a = 10
print(id(a))
update(a)
print("Value outside function is", a)

x = 11
print(id(x))
update(x)
print("Value outside function is", x)

print('\n############MUTABLE LIST - PASS BY REFERENCE##################')


def update(lst):
    print(id(lst))
    lst[1] = 25
    print(id(lst))
    print("List value inside function is", lst)


lst = [10, 20, 30]
print(id(lst))
update(lst)
print("List value outside function is", lst)

print('\n############ARGUMENTS##################')


def person(name, age):
    print("Name is:", name)
    print("Age is:", age)


person("Python", 22)


def person(name, age=18):
    print("Name is:", name)
    print("Age is:", age)


person("Python")
person("Python", 24)


def summation(a, *b):
    print("Addition of numbers is:", a + sum(b))


summation(5, 4)
summation(5, 5, 5, 5)

print('\n############KEYWORS VARIABLE LENGTH ARGUMENTS##################')


def person(name, **kwargs):
    print("Name is:", name)
    print("Data is:", kwargs)


person('Python', age=20, city='Mumbai', country='India', mobile=9876543210)
