# Labmda function / Anonymous functions
# filter - map - reduce Google Concept

from functools import *


def square(num):
    return num * num


print('\n##############################')
num = 5
result = square(num)
print("Square of {} is {}".format(num, result))

f = lambda a: a * a

add = lambda a, b: a + b

print('\n##############################')
num = 5
result = f(num)
print("Lambda - Square of {} is {}".format(num, result))

print('\n##############################')
num1 = 5
num2 = 10
result = add(num1, num2)
print("Lambda - Addition of {} & {} is {}".format(num1, num2, result))

print('\n##############################')


def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 != 0


nums = [3, 2, 6, 8, 4, 6, 2, 9]
evens = list(filter(is_even, nums))
odds = list(filter(is_odd, nums))

print("List of even numbers: ", evens)
print("List of odd numbers: ", odds)


print('\n#############FILTER#################')
nums = [3, 2, 6, 8, 4, 6, 2, 9, 11, 14, 18, 9, 13, 17, 21]
evens = list(filter(lambda n: n % 2 == 0, nums))
odds = list(filter(lambda n: n % 2 != 0, nums))

print("List of even numbers: ", evens)
print("List of odd numbers: ", odds)

print('\n#############MAP#################')
evenmap = list(map(lambda n: n * 2, evens))
oddmap = list(map(lambda n: n * 2, odds))

print("Double of even numbers: ", evenmap)
print("Double of odd numbers: ", oddmap)

print('\n#############REDUCE#################')
evenreduce = reduce(lambda a,b: a + b, evenmap)
oddreduce = reduce(lambda a,b: a + b, oddmap)

print("Total of even numbers: ", evenreduce)
print("Total of odd numbers: ", oddreduce)
