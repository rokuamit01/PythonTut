#import array as arr
from array import *

vals = array('i',[5,9,8,4,2,1,8])
print(vals)
print(vals.buffer_info())

vals.reverse()
print(vals)
print(vals.buffer_info())

for i in range(7):
    print(vals[i])

print('\n##############################')
for i in range(len(vals)):
    print(vals[i])

print('\n##############################')
for e in vals:
    print(e)

print('\n##############################')
newArr = array(vals.typecode, (a for a in vals))
for e in newArr:
    print(e)

print('\n##############################')
newArr2 = array(vals.typecode, (a*a for a in vals))
for e in newArr2:
    print(e)

print('\n##############################')
chrs = array('u',['a','e','i','o','u'])
print(chrs)
print(chrs.buffer_info())

print('\n##############################')
arr = array('i',[])
size = int(input('Enter the length of the array: '))

for i in range(size):
    val = int(input('Enter the next item: '))
    arr.append(val)

print(arr)

print('\n##############################')
searchVal = int(input('Enter the value for search: '))
k=0
for e in arr:
    if e==searchVal:
        print('Item found at index:', k)
        break
    k+=1

print('\n##############################')
print('Item found at index:', arr.index(searchVal))