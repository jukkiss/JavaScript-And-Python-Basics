lentokentat = {}

while True:
    inputti = input(
        'Hae tai syötä lentokenttä komennoilla: "hae" ja "syötä". Voit lopettaa ohjelman komennolla "lopeta": ')
    if inputti == "syötä":
        kenttakoodi = input('Syötä kentan ICAO-koodi: ')
        kenttanimi = input('Syötä kentän nimi: ')
        lentokentat[kenttakoodi] = kenttanimi
    elif inputti == "hae":
        kenttahaku = input("Hae lentokenttää ICAO-koodilla: ")
        if kenttahaku in lentokentat:
            print(f"lentokentän nimi on {kenttanimi}")
    elif inputti == "lopeta":
        break
    else:
        print("Syötä oikea komento.")
