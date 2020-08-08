#fibonacci
list = [0, 1]
print(list[-1])
print(list[-2])
for i in range(48):
    list.append(list[-1]+list[-2])
print('bye')
print(list)

print('\n##############################')


def fib(limit):
    a, b = 0, 1
    print('\n')
    if limit == 1:
        print(a, ' ', end="")

    elif limit == 2:
        print(a, ' ', end="")
        print(b, ' ', end="")

    else:
        print(a, ' ', end="")
        print(b, ' ', end="")

    for i in range(2, limit):
        c = a + b
        a = b
        b = c
        print(c, ' ', end="")


fib(10)
fib(1)
fib(2)