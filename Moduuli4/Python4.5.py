tunnus = "python"
salasana = "rules"

kay = input("Anna käyttäjätunnus: ")
sala = input("Anna salasana: ")

yritykset = 5

while yritykset > 0:
    if kay == tunnus and sala == salasana:
        print("Tervetuloa.")
        break
    else:
        print("Pääsy evätty")
        yritykset -= 1
        if yritykset == 0:
            print("Yritykset loppu")
            break
        kay = input("Anna käyttäjätunnus: ")
        sala = input("Anna salasana: ")



