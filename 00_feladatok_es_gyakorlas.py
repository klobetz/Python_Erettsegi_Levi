# # Írj egy Python programot, amely bekér három számot a felhasználótól
# # és kiírja a képernyőre a legkisebb értéket ezek közül!
#
#
# #vagy így de ez nem elegáns
# #szam = 9999999999999999
#
# import sys
# szam = sys.maxsize
# print(szam)
# for i in range(3):
#     valasz = int(input('Kérek egy számot:'))
#     if valasz < szam:
#         szam = valasz
# else:
#     print(szam)
#
# #vagy beépített függvénnyel
# valasz1 = int(input('Kérek egy számot:'))
# valasz2 = int(input('Kérek egy számot:'))
# valasz3 = int(input('Kérek egy számot:'))
#
# print(f'a legkisebb érték: {min(valasz1,valasz2,valasz3)}')
# print(f'a legnagyobb érték: {max(valasz1,valasz2,valasz3)}')
#
#
#
# # Írj egy Python programot, amely bekér három számot a felhasználótól
# # és kiírja a képernyőre a legnagyobb értéket ezek közül!
# szam = 0
# for i in range(3):
#     valasz = int(input('Kérek egy számot:'))
#     if valasz > szam:
#         szam = valasz
# else:
#     print(szam)
#
#
#
#
#
#
#fibonacci
valasz = int(input("kérek egy számot: "))

elsoelem = 0
masodikelem = 1
harmadikelem = 0
fibonacci = [0, 1]
for elem in range(valasz):
    harmadikelem = elsoelem+masodikelem
    fibonacci.append(harmadikelem)
    elsoelem = masodikelem
    masodikelem = harmadikelem

print(fibonacci)

#vagy

valasz = int(input("kérek egy számot: "))

fibonacci2 = [0, 1]
for elem in range(valasz):
    harmadikelem2 = fibonacci2[0+elem]+fibonacci2[1+elem]
    fibonacci2.append(harmadikelem2)
print(fibonacci2)

