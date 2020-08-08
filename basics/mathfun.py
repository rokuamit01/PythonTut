print(__name__)


def add(a, b):
    print('Addition of values is:', a + b)


def multiply(a, b):
    print('Multiplication of values is:', a * b)


def main():
    print('In mathfun __main__')
    add(5, 6)
    multiply(5, 6)


if __name__ == "__main__":
    main()

