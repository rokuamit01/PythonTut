nums = [1, 2, 3, 4, 5, 6]

it1 = iter(nums)

print(it1.__next__())
print(it1.__next__())
print(next(it1))

print('\n###################')
for i in nums:
    print(i)

print('\n###################')
for i in it1:
    print(i)


class IteratorTopTen:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            print('Max value reached.')
            raise StopIteration


print('\n###################')
values = IteratorTopTen()
print(values.__next__())
print(values.__next__())
print(next(values))

print('\n###################')
for i in values:
    print(i)

print('\n###################')

print(values.__next__())
print(values.__next__())
print(next(values))
