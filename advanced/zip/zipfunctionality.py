

names = ("Navin", "Kiran", "Harsh","Navin","Harsh")
company = ("Dell", "Apple", "MS","Google","MS")
location = ("HYD", "USA", "EUR", "IND", "AUS")
sal = ("1M", "2M", "3M")

print('##########################')
zipped = list(zip(names, company))
print(zipped)

print('##########################')
zipped = list(zip(names, company, location))
print(zipped)

print('##########################')
zipped = list(zip(names, company, location, sal))
print(zipped)

print('##########################')
zipped = set(zip(names, company))
print(zipped)

print('##########################')
zipped = set(zip(names, company, location))
print(zipped)

print('##########################')
zipped = set(zip(names, company, location, sal))
print(zipped)

print('##########################')
zipped = dict(zip(names, company))
print(zipped)

print('##########################')
zipped = dict(zip(names, location))
print(zipped)

print('##########################')
zipped = dict(zip(company, location))
print(zipped)

print('##########################')
zipped = dict(zip(location, sal))
print(zipped)

print('##########################')
zipped = zip(names, company)
for (a, b) in zipped:
    print(a, b)

print('##########################')
zipped = zip(names, company, location)
for (a, b, c) in zipped:
    print(a, b, c)

print('##########################')
zipped = zip(names, company, location, sal)
for (a, b, c, d) in zipped:
    print(a, b, c, d)
