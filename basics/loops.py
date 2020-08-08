
i = 1
while i <= 10:
    print('Counter: ', i)
    i = i + 1

while i >= 1:
    print('Counter: ', i, " ", end="")
    i=i-1

print('##############################')
i = 1
j = 1
while i <= 5:
    print('Counter: ', i)
    j = 1
    while j <= 4:
        print('Inner counter: ', j)
        j = j+1
    i = i + 1

print('##############################')
i = 1
j = 1
while i <= 5:
    print('# ')
    j = 1
    while j <= 4:
        print('# ', end="")
        j = j+1
    i = i + 1

print('\n##############################')
i = 1
while i <= 4:
    print('# ' * 5)
    i = i + 1

print('\n##############################')
i = 1
while i <= 100:
    if (i%3 != 0) and (i%5 != 0):
        print('Number is: ', i)
    i = i + 1

print('\n##############################')
x = ['Python', 65, 2.5]

for i in x:
    print(i)

print('\n##############################')
x = 'Python'

for i in x:
    print(i)

print('\n##############################')
for i in [2,6,'Paul']:
    print(i)

print('\n##############################')
for i in range(10):
    print(i)

print('\n##############################')
for i in range(11,21,1):
    print(i)

print('\n##############################')
for i in range(20,10,-1):
    print(i)

print('\n##############################')
for i in range(1,21):
    if i%5 != 0:
        print(i)