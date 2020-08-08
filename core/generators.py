#  Fetching values from database one by one


def topten():

    n = 1

    while n <= 10:
        sq = n * n
        yield sq
        n += 1


values = topten()
print(values.__next__())
print(values.__next__())
print(values.__next__())
print(values.__next__())
print(next(values))
print(next(values))

print('\n###################')
for i in values:
    print(i)

print(next(values))
