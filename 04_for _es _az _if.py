#vagyünk fel egy int típusú listát és töltsük fel számokkal

list = [5, 47, 8, 54, 6, 2, 15, 4, 1, 25, 10, 65, 17, 321]

# írasuk ki a 20 nál kisebb szhámokat
for listaelem in list:
    if listaelem <= 20:
        print(listaelem, end=', ')

#írjuk ki a 10 és a 20 közötti számokat
print()
for listaelem in list:
    if listaelem > 10 and listaelem < 20:
        print(listaelem, end=', ')

#írjuk ki a 10 kisebb és a 20 nál nagyobb számokat
print()
for listaelem in list:
    if listaelem < 10 or listaelem > 20:
        print(listaelem, end=', ')

#Írjuk ki a lista elemeit meddig nem találok 10-et
print()
for listaelem in list:
    print(listaelem, end=', ')
    if listaelem == 10:
        break
print('\nVégeztem!!!! elértem a megadott számot!')