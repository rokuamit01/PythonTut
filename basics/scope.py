a = 10
b = 25
print("Value of outside a: ", a, end="")
print("Id of outside a: ", id(a))
print("Value of outside b: ", b)

print('\n############LOCAL/GLOBAL VARIABLE##################')


def something():
    a = 15
    global b
    print("Value of something a: ", a)
    print("Value of something b: ", b)
    b = 30
    print("Value of something b: ", b)

    x = globals()['a']
    print("Id of something a: ", id(x))
    globals()['a'] = 40
    print("Value of something a: ", a)


something()
print("Value of outside a: ", a)
print("Value of outside b: ", b)

print('\n############LPASSING LIST AS ARGUMENT##################')


def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even+=1
        else:
            odd+=1

    return even, odd


lst = [20, 25, 14, 19, 16, 24, 28, 47, 26]
even, odd = count(lst)

print("Even count is: ", even)
print("Odd count is: ", odd)
print("Even : {} and Odd : {}".format(even, odd))