# #feladatleírás
#
# # while feltétel
# #     ciklustörzs


# valasz = int(input('Kérek egy számot: '))
# kezdo = 0
# osszeg = 0
# while kezdo <= valasz:
#     osszeg += kezdo
#     kezdo +=1
# print(osszeg)
#
# #ugyan ez for-ral?
# print()
# osszeg2 = 0
# for i in range(valasz+1):
#     osszeg2 += i
# print(f'a sorozat összege: {osszeg2}')


#középen tesztelős ciklus:
osszeg3 = 0
while True:         # a True azt jelenti hogy igaz azaz újra és újra kérje be
    bemenet = input('Kérek egy számot: ')
    if bemenet == '':
        break
    osszeg3 += int(bemenet)
print(f'A megadott számok összege: {osszeg3}')

#hátul tesztelős ciklus
while True:
    jelszo = input('Kérem a jelszót: ')
    jelszoujra = input('Jelszó megerősítés: ')
    if jelszo == jelszoujra:
        break
    print('A két jeszó nem egyezik meg!!!! Próbáld újra!')
print('Köszönöm! A jelszvakat tároltuk az adatbázisban!')