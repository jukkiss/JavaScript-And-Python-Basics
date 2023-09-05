import random as r


def heitto(tahkonoppa):
    noppa = r.randint(1, tahkonoppa)
    return noppa

tahkonoppa = int(input("Syötä tahkot: "))
silmaluku = int(input("Anna maksimi silmäluku: "))

while True:
    heitot = heitto(tahkonoppa)
    print(heitot)
    if heitot == silmaluku:
        break