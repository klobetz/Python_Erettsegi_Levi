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
