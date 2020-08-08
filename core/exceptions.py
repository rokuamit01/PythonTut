#  Compile Time (Syntax Error), Logical, Run Time Error

resourceOpen = True

try:
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    resourceOpen = True
    print(r"Database connection established.")
    print('Division is:', a / b)
except ZeroDivisionError as e:
    print(r"Division denominator can't be zero. Error -> ", e)
    if resourceOpen == True:
        print(r"Database connection closed.")
        resourceOpen = False
except ValueError as e:
    print(r"Invalid input by user. Error -> ", e)
    if resourceOpen == True:
        print(r"Database connection closed.")
        resourceOpen = False
except Exception as e:
    print(r"Something went wrong. Error -> ", e)
    if resourceOpen == True:
        print(r"Database connection closed.")
        resourceOpen = False

finally:
    if resourceOpen == True:
        print(r"Database connection closed.")

