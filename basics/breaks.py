x = int(input('How many candies you want?: '))

MAX = 20

i = 1
while i <= x:
    if i > MAX:
        print('Out of stock')
        break
    print('Candy# ',i)
    i=i+1
print('\n##############################1')
for i in range(1,101):
    if i%3!=0 and i%5!=0:
        print(i)

print('\n##############################2')
for i in range(1,101):
    if i%3==0 and i%5==0:
        continue
    print(i)

print('\n##############################3')
for i in range(1,101):
    if i%2==0:
        pass
    else:
        print(i)