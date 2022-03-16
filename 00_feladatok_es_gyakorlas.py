# Írj egy Python programot, amely bekér három számot a felhasználótól
# és kiírja a képernyőre a legkisebb értéket ezek közül!


#vagy így de ez nem elegáns
#szam = 9999999999999999

import sys
szam = sys.maxsize
print(szam)
for i in range(3):
    valasz = int(input('Kérek egy számot:'))
    if valasz < szam:
        szam = valasz
else:
    print(szam)

#vagy beépített függvénnyel
valasz1 = int(input('Kérek egy számot:'))
valasz2 = int(input('Kérek egy számot:'))
valasz3 = int(input('Kérek egy számot:'))

print(f'a legkisebb érték: {min(valasz1,valasz2,valasz3)}')
print(f'a legnagyobb érték: {max(valasz1,valasz2,valasz3)}')



# Írj egy Python programot, amely bekér három számot a felhasználótól
# és kiírja a képernyőre a legnagyobb értéket ezek közül!
szam = 0
for i in range(3):
    valasz = int(input('Kérek egy számot:'))
    if valasz > szam:
        szam = valasz
else:
    print(szam)






