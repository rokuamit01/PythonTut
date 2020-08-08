
for i in range(4):
    for j in range(4):
        print('# ',end="")
    print('')

print('\n##############################')

for i in range(4):
    for j in range(i+1):
        print('# ',end="")
    print('')

print('\n##############################')

for i in range(4):
    for j in range(4-i):
        print('# ',end="")
    print('')

print('\n##############################')

for i in range(4):
    for j in range(4-i):
        print(i+j+1, ' ',end="")
    print('')

print('\n##############################')

lst1=['A','B','C','D']
lst2=['P','Q','R','S']
print(lst1)
print(lst2)
for i in range(4):
    for j in range(4):
        if j <= i:
            print(lst1[j],' ',end="")
        else:
            print(lst2[j-1],' ',end="")
    print('')