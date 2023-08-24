
luvut = []

luku = input("Anna luku: ")

while luku != luku.endswith(" "):
    luvut.append(luku)
    if luku.startswith(" "):
        luvut.sort()
        print(f"Pienin listan luku on {luvut[1]} ja isoin {luvut[-1]}.")
        break
    print(luku)
    luku = input("Anna luku: ")