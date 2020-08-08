import sys

x = int(sys.argv[1])
print('Entered number is:', x)
result = x % 2

if result == 0:
    print('I am right')
    print('I am still under if')
    print('Entered number is even.')

if result != 0:
    print('I am wrong')
    print('I am still under else')
    print('Entered number is odd.')

print('##############################')

if result == 0:
    print('Entered number is even.')
else:
    print('Entered number is odd.')

print('I am outside if-else')
print('Bye')

print('##############################')

if result == 0:
    print('Entered number is even.')
    if x > 5:
        print('Entered number is greater than 5.')
    else:
        print('Entered number is less than 5.')
else:
    print('Entered number is odd.')
    if x > 6:
        print('Entered number is greater than 6.')
    else:
        print('Entered number is less than 6.')

print('I am outside if-else')
print('Bye')

print('##############################')
a = int(sys.argv[2])
if a == 1:
    print('One')
elif a == 2:
    print('Two')
elif a == 3:
    print('Three')
elif a == 4:
    print('Four')
else:
    print('Wrong Input')