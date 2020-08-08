# Decorators helps in adding extra features to an existing function - takes function as a parameters


def div(a, b):
    if a < b:
        a, b = b, a
    print('Division result is', a / b)


def subtraction(a, b):
    print('Subtraction result is', a - b)


def smart_subtraction(func):
    def inner(x, y):
        if x < y:
            x, y = y, x
        return func(x, y)

    return inner


div(2, 4)
div(4, 2)
subtraction(4, 2)
subtraction(2, 4)

subtraction = smart_subtraction(subtraction)
subtraction(2, 4)
