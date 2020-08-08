# Calling function from itself. Default recursion depth is 1000
import sys

print(sys.getrecursionlimit())

sys.setrecursionlimit(1500)

print(sys.getrecursionlimit())


def factorial(num):
    res = 1
    print("Given number is: ", num)

    for i in range(1, num + 1):
        res = res * i

    return res


print("Recursion result is:", factorial(5))


def fact(num):
    if num == 0:
        return 1

    return num * fact(num - 1)


print("Recursion result is:", fact(4))