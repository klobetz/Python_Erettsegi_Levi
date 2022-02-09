#írd ki a számokat 1-10-ig
print(1,2,3,4,5,6,7,8,9,10)
#vagy
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(7)
print(9)
print(10)

#for ciklus segítségével:
print()
for i in [1,2,3,4,5,6,7,8,9,10]:        #lista létrehozása
    print(i)

#írjuk ki hogy Szeretek programozni
print()
for i in [1,2,3,4]:
    print('szeretek programozni')

# lista kiszervezése változóba:
print()
lista = [1,2,3,4,5,6,7,8,9,10]
for i in lista:
    print(i, end=', ')                   #egy soros kiíratás

# a range használata
# írd ki a számokat 1-10-ig
print()
for i in range(10):                     # a renge(10) => 0-9-ig írja ki a számokat (indexelés)
    print(i, end=', ')

# írd ki a számokat 1-10-ig
print()
for i in range(1,11):
    print(i, end=', ')

# írd ki a számokat 5-10-ig
print()
for i in range(5,11):
    print(i, end=', ')

# írasuk ki a páros számokat 1-10-ig
print()
for i in range(2,11,2):
    print(i, end=', ')

# páratlanok kiírása 1-10-ig
print()
for i in range(1,11,2):
    print(i, end=', ')
