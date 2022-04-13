# egységben kezelt sztringek

sztring = "Járványhelyzet"
print(sztring.upper())      #nagybetűs
print(sztring.lower())      #kisbetűs
print(sztring)              #eredeti azaz a változó értéke nem módosul
print(sztring.swapcase())   #kicsiből nagy betű a nagyból meg kicsi


#részenként kezelve
print(sztring[1])           #elem kiíratása 0-tól indexel
print(len(sztring))         # a sztring hossza ami 1-től számol
print(sztring[-1])          # az utolsó karakter kiíratása
print(list(enumerate(sztring)))     #az indexek kiíratása a sztingben

hossz = len(sztring)        #sztring hossza
utolso = sztring[hossz-1]   #az utolsó elem megkeresése index miatt a -1
print(hossz)                #kiíratás
print(utolso)               #kiíratás

#vagy egy sorban
print(sztring[len(sztring) - 1])        #a kettő ugyan az!
print(sztring[13])

#szting bejársa
#for-ral

for elem in sztring:
    print(elem,end=" ")

print()
#while-al
i=0
while i < len(sztring):
    print((i+1), sztring[i])

    i+=1

#sztring szeletelés
gyumolcs = "szederfa"
print(gyumolcs[0:3])            #az elejétől a 3.karakterig kiír
print(gyumolcs[3:400])          #ez nem fut hibára kiírja végig

#in not in oprátorok használata

print('a' in gyumolcs)      #az a megtalálható-e a gyümölcs változóban?

if 'a' in gyumolcs:
    print("igen van benne 'a'")

print('a' not in gyumolcs)

if 'a' not in gyumolcs:         #csak akkor írja ki ha van else ert az értéke false
    pass
else:
    print("A szóban szerele az 'a' kerekter")

# kérjünk be a felhasználótól egy karaktert és ellenőrizzük le, hogy szerepel-e a szederfa szóban vagy sem
#ha szerepel akkor írassuk kihogy hányadik helyen szerepel az adott karakter
valasz = input("Kérek egy karaktert: ")

if valasz in gyumolcs:                  #megvizsgálom hogy van e benne
    print("Igen szerepel benne")
    hanyadik = 0
    for i in gyumolcs:                  #ha van benne akkor megnézem hogy hányadik
        if valasz==i:
            print(f"az adott karakter a {hanyadik+1} pozíción szerepel")
            #break      #ez csak akkor kell ha csak az első találatig akarok menni
        hanyadik+=1
else:
    print(f"Nem nem szerepel benne a {valasz}")


#házi ugyanez while-al

#beépített metódus használata
print(gyumolcs.find('k'))           # ha nincs benne akkor -1 -el tér vissza
print(gyumolcs.find('e')+1)         # ha van benne akkor kiírja az indexét és ehez hozzáadunk egyet és így pozíciót kapok

#split metódus darabolás
mondat = "Én már kezdem érteni, ezeket a műveleteket"
print(mondat.split())
print(type(mondat.split()))
