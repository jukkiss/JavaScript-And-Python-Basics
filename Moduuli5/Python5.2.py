lista = []
totta = True
inputti = input("Anna luku: ")

while totta:
    lista.append(inputti)
    inputti = input("Anna luku: ")
    if inputti == "":
        lista.sort(reverse=True)
        print(lista[0:4])
        break