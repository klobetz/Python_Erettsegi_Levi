#booleam típus 2 db True és a False
#type(True)   class 'bool'
#type(False)  class 'bool'

#ÖSSZEHASONLÍTÓ OPERÁTOROK:
    #Egyenlő a == b
    #Nem egyenlő: a != b            negátolás!!!!
    #Kisebb mint: a < b
    #Nagyobb mint: a > b
    #Kisebb vagy egyenlő: a <= b
    #Nagyobb vagy egyenlő: a >= b

#LOGIKAI OPERÁTOROK:
    #És => and
    #Vagy => or
    #tagadás => not

# feltételes végrehajtás (az if használata)
#vegyünk fel két változót és adjunk neki értéket. döntsük el hogy ha az a < b akkor azt írasuk ki!
a=25
b=33
if a<b:
    print(f'a {a} kisebb mint  a {b} ')


#kérjünk be egy számot a felhasználótól és döntsük el róla hogy páros vagy páratlan.
    #ebben az eseten csak a páros számokat vizsgálom
valasz = int(input('Kérek egy számot (csak páros lehet): '))
if valasz % 2 == 0:
     print(f'A megadott szám páros')


    #mostr javítjuk a programunkat és megnézzük mins a kettő ágat
        #igaz vagy hamis

valasz2 = int(input('Kérek egy második számot (itt bármi lehet): '))

if valasz2 % 2 == 0:
    print(f'A megadott szám {valasz2} ami páros')         #igaz ág   (vagy ez fut le)
else:
    print(f'A megadott szám {valasz2} ami páratlan')      #hamis ág  (vagy ez fut le)

# kérjünk be egy számot és döntsük el róla hogy negtív vagy pozitív:

pozitiv = int(input('Kérek egy számot: '))
if pozitiv > 0:
    print(f'A megadott szám {pozitiv} ami pozitív')
else:
    print(f'A megadott szám {pozitiv} ami negatív')


#LÁNCOLT FELTÉTELES UTASÍTÁS:
    #szerinted melyik a helyes válasz? Pl: a vagy b vagy c

valasztasok = input('melyi a helyes válasz? "a" vagy "b" vagy "c": ')

if valasztasok == 'a':
    print('az "a" választ írtad be')
elif valasztasok== 'b':
    print('az "b" választ írtad be')
elif valasztasok == 'c':
    print('az "c" választ írtad be')
else:
    print('rossz választ adtál meg')

#BEÁGYAZOTT FELTÉTELES UTASÍTÁS:
    # kérjünk be egy számot és döntsük el róla hogy negtív vagy pozitív vagy 0-a:

valasz3 = int(input('Kérek egy számot: '))

if valasz3 > 0:
    print(f'A megadott szám {valasz3} ami pozitív')
else:
    if valasz3 < 0:
        print(f'A megadott szám {valasz3} ami negatív')
    else:
        print(f'A megadott szám {valasz3} ami se nem pozitív se nem negatív')

#házi és ellenőrzés
tiznelnagyobb = int(input('Kérek egy egész számot:'))

if tiznelnagyobb > 0 and tiznelnagyobb < 10:
    print('A szám 0-a és 10 közé esik')
else:
    print('A szám 10-nél nagyobb')


