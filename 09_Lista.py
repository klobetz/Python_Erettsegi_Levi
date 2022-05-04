#lista létrehozása
ureslista=[]
szamok=[5,87,6,32,145,6,32]
szoveg=["alma","virág","kutya","ember"]
listaalistaban = [4,8,6,22, [4,8,5,6,], 85]
vegyes = [5, "barack", 3.8, [412, "szép", 8.4]]


#lista elérése
print(ureslista, szamok, szoveg,listaalistaban,vegyes )

#lista eleminek az elérése:
#indexelés ezért az eredmény 32.
print(szamok[3])
print(szamok[-1])       #utolsó elem
print(szamok[1-3])      #a 2-. elemet íratja ki azaz 145


#minden elem kiíratása
#ciklussal
for elemek in szamok:
    print(elemek)

print(*szamok)      #lista bejátása ciklus nélkül
print(*listaalistaban)
print(listaalistaban[5])

#print(szamok[25])       # ez hiba IndexError: list index out of range

#lista hossza
print(len(szamok))      # hány eleme van a listának 6 db nem index

print(len(vegyes))      #4 az eredmény a listában ha van egy másik lista az csak egy elem!!!!!!

#keresés a listában
print(32 in szamok)         #va e benne 32 érték eredmény True ha van benne

# vizsgálat ha van és ha nincs
if 32 in szamok:
    print("van találat")
else:
    print("nincs találat")

# lista műveletek:
#összeadás
osszeadas = szamok + szoveg
print(osszeadas)
print(*osszeadas)

#szorzás *
szorzas = szamok*2
print(szorzas)

#szeletelés
print(szamok[1:4])
print(szamok[:4])
print(szamok[4:])

#elemek módosítása felülírása
print(*szoveg)
szoveg[2]= "egésznap"
print(szoveg)

#elem beszúrása de ez karakterenként
szoveg[1:1] = "FALIÓRA"
print(szoveg)

# elem törlése
print(szamok)
del szamok[2]
print(szamok)

del szoveg[1:8]
print(szoveg)

#hozzáfűz az utolsó helyre
szoveg.append("valami")
print(szoveg)

print("!"*50)
# objektumok és hivatkozások
#sztring esetében: ugyan arra az objektumra mutat az alábbi módon bizonyítjuk
a = "valami"
b = "valami"
print(a==b)
print(a in b)

print("!"*50)
#viszont a lista esetben külön objektumra mutata!!! az alábbi módon bizonyítjuk
list1 = [1,2,3,4,]
list2 = [1,2,3,4,]

print(list1==list2)
print(list1 in list2)

print("!"*50)

#lista klónozása
a = ["egy","kettő"]
b = a[:]

print(b)

a.append("három")

print(a)
print(b)

# lista és a for ciklus használata
#készítünk egy listát majd az elemeket szorozzuk meg 2-vel és írassuk ki őket az elemmel együtt!
print("%"*50)
szorzat = [1,2,3,4,5,6]

for i in szorzat:
    print(f"az eredeti szám: {i} => {i*2}")

for (i, erek) in enumerate(szorzat):
    print(f"a sorozat indexe: {i} az adott indexen az eredeti érték: {erek} aminek a kétszerese: {erek*2}")

#ugyanez szöveggel:
print("-"*50)
szöveg = ["szöveg","kutya", "virág", "alma"]
for (i, erek) in enumerate(szöveg):
    print(i,erek)

print("-"*50)
# lista mtódusok
mlista = []
mlista.append(85)           #elem hozzáfűzése (mindig az utoldó pozícióra)
mlista.append(65)
mlista.append(4)
mlista.append(418)
mlista.append(12)
print(mlista)

mlista.insert(2,45)         #elem beszúrása az adott potícióra
print(mlista)

print("-"*50)
sorbarendezve = sorted(mlista)
print(sorbarendezve)        #növekvő sorrend az eredeit lista nem módosul!!!!
print(mlista)

print(sorted(mlista))
print(mlista)
print("-"*50)

#lista megfordítása az eredeti lista nem változik
print(sorted(mlista, reverse=True))
print("-"*50)

mlista.reverse()            #elemek megfordítása de az eredeti lista módosul!!!!!!!!
print(mlista)

mlista.sort()               #sorba rendez de az eredeti lista módosul!!!!!!!!
print(mlista)