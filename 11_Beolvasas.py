#beolvasás:

with open("nevek_sima.txt", encoding="utf8") as fajl:       #ez a "fajl" válltozó bármi lehet álltalában "f"-nek használják
    sor = fajl.read()

print(sor)
print(type(sor))

#listába beolvasás
print("-"*50)
with open("nevek_sima.txt", encoding="utf8") as f:
    sor = f.read()
    lista = sor.split()             #split() feldarabolja a szöveget az enterek mentén vagy a szóközök mentén
                                    #és egy listába helyezi el szavanként!!!!!!!!
print(lista)
print(type(lista))

for elem in enumerate(lista):
    print(elem)

# soronkéni beolvasás azaz csak bizonyos sorok beolvasása
print("-"*50)
with open("nevek_sima.txt", encoding="utf8") as f:
    sor1 = f.readline().strip().split()
    sor2 = f.readline().split()
    sor3 = f.readline().split()

print(sor1)
print(sor3)

#beolvasás soronként istába tárolva
print("-"*50)
lista2 = []                             #üres lista készítése
with open("nevek_sima.txt", encoding="utf8") as f:      #fájl megnyitása
    elsosor = f.readline()              #első sor kiszedése
    for elem in f:                      #fájl bejárása
        sor = elem.split()              #sor változóba darabol
        lista2.append(sor)              #hozzáad a listához

print(elsosor)
print(lista2)

print("-"*50)
for nev in lista2:
    print(nev)

print("-"*50)
# csak a vezetéknevek kiíratása
for nev in lista2:
    vnev = nev[0]
    print(vnev)

print("-"*50)

# csak a keresztnevek kiíratása
for nev in lista2:
    knev = nev[1]
    print(knev)

print("-"*50)