

def listalaskin(lista):
    summa = 0
    for nro in lista:
        summa = summa + nro
    return(summa)

lista = [1, 2, 3, 4, 5, 6, 9, 10]

x = listalaskin(lista)

print(x)