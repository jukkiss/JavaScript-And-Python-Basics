import random

arvaus = input("Anna numero 1-10: ")

koneen_luku = random.randint(1, 10)

while arvaus != koneen_luku:

    arvaus = int(arvaus)
    if arvaus == koneen_luku:
        print("Arvasit oikein!")
        break
    elif arvaus < koneen_luku:
        print("Liian pieni arvaus")
    elif arvaus > koneen_luku:
        print("Liian suuri arvaus")
    arvaus = input("Anna numero 1-10: ")
