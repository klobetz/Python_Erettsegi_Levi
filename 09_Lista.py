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






