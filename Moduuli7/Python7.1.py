vuodenajat = ("Kevät", "Kesä", "Syksy", "Talvi")

kysyttynro = int(input("Anna kuukauden numero (1-12): "))

if kysyttynro == 1 or kysyttynro == 2 or kysyttynro == 12:
    print(vuodenajat[-1])
elif kysyttynro == 3 or kysyttynro == 4 or kysyttynro == 5:
    print(vuodenajat[-4])
elif kysyttynro == 6 or kysyttynro == 7 or kysyttynro == 8:
    print(vuodenajat[-3])
elif kysyttynro == 9 or kysyttynro == 10 or kysyttynro == 11:
    print(vuodenajat[-2])
else:
    print("Annettu syöte ei kelpaa.")
    

