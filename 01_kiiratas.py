# kiíratás:
print("Ez az első programom") #vagy
print('\nEz is szöveg')

#több soros megjelenítés:
print("""\nez a szöveg         
több sorban
jelenik meg.""")               #\n az sortörést jelenti

# Értéktípusok:
15          #int
'szöveg'    #str (string)
3.5         #float (lebegő pontos)
3,5         #értékpár

# változók létrehozása és értékadás
print()
a = 'változób tárolt string'        #változó létrehozása és értékadás
print(a)            #az a változó kiíratása a képernyőre

x = 15
y = 3.5
z = 'szöveg'

print(a,x,y,z)

# változó értékének a növelise
b = 1
print(b)
b = b + 1  # a b változóban tárolt adat értékének a növelése eggyel
print(b)
# vagy
b += 1  # a b változóban tárolt adat értékének a növelése eggyel
print(b)
# b=+1       #ha ezt így írod akkor olyan mintha beállítanád neki a b = 1 azaz b értéke egy lesz

#Változó típusának a megváltoztatása
print()             #sortörés
ido = 'süt a nap'   #str
print(ido)
ido= 'felhős'       #érték megváltoztatása
print(ido)
ido = 1985          #típus változtatása
print(ido)

#kiértékelés len beépített függvény használata
sajatnevem = 'Klobetz Ákos'
print(len(sajatnevem))

#összeadás
d=8
c=5
e=d+c
print(e)        #változóba eltárolva
print(d+c)      #kiíratás közben

#szöveg hozzáadása a kiíratáshoz
print('\nA két szám összege: '+str(e))        #típuskonverzió str(e) (kasztolás)
#vagy
print('\nA két szám összege: ', e)            #int típusként való kiíratás

print(f'\nA két szám összege: {e}')           #sztring interpoláció (a szövegbe bele tudom illeszteni  aváltozómat akár
                                              # többet is!)

#típukonverziós függvény ami nem egyenlő a változó típusával!!!
#ezt a terminál ablakban futatom!!!
int(15)
15
float(15)
15.0
str(15)
'15'

#műveletek:

# összeadás: +
# kivonás: -
# szorzás: *
# osztások
o=c/3       #maradékos osztás
print(o)

o=c//3
print(o)    #egészre kerekít

h=c**2
print(o)    #hatványozás

o=c%d
print(o)    #osztás maradéka

# a zárójelekkel módosítható ez eredmény kiértékelése!!!!
# n=5
# n= 3*n+1 eredmény 16
# de ha zárójelezek:
# n=5
# n= 3*(n+1) eredmény 18

#szövegösszefűzés:
vnev = 'Klobetz'
knev = 'Ákos'
print(vnev + ' ' + knev)

#adat bekérés a felhasználótól
input('Kérek egy adatot:')

#adat bekérés a felhasználótól és változóba tárolása
valasz=input('Kérek egy adatot:')
print(f'A megadot adat: {valasz}')