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
print(13%7)

print()
print(*range(1,11))         #egy sorban a számok kiíratása

#írjuk ki a számokat 1-10 ig és szóljunk a felhaszálónak, hogy kész!
print()
for i in range(1,11):
    print(i, end=' ')
else:
    print('vége a ciklusnak')

#szöveg kezelése:
for i in "szöveg":
    print(i)

#szöveg kiíratása listából
gyumolcsok = ['alma', 'körte', 'banán', 'szilva', 'narancs', 'kiwi']
for i in gyumolcsok:
    print(i, end=', ')

#írasuk ki a lista hosszát. hány elem van a listában!
print(f'\nA listában szereplő elemek száma: {len(gyumolcsok)} db')

#2 db lista: tulajdonság és gyümölcs
#írjuk ki az egyes tulajdonsághoz a gyümölcsök2-t

tulajdonsagok = ['érett', 'nagy', 'édes']

for i in tulajdonsagok:
    for j in gyumolcsok:
        print(i, j)
print()
for i in gyumolcsok:
    for j in tulajdonsagok:
        print(i, j)