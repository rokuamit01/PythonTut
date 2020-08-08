
print(__name__)

def factorial(num):
    res = 1
    print("Given number is: ", num)

    for i in range(1,num + 1):
        res = res * i

    return res


num = int(input("Enter a number to evaluate factorial: "))
result = factorial(num)
print("Factorial of {} is {}".format(num, result))