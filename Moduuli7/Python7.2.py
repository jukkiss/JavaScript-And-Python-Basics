

nimet = set()

while True:
    nimipyynto = input("Anna nimi: ")
    if nimipyynto == "":
        break
    if nimipyynto in nimet:
        print("Aiemmin syötetty nimi")
    elif nimipyynto not in nimet:
        print("Uusi nimi")
    nimet.add(str(nimipyynto))

for i in nimet:
    print(i)
