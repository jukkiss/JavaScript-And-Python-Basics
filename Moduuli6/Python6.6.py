import math

def laskehinta(halkaisija, hinta):
    pinta = math.pi * ((halkaisija / 2) ** 2)
    pintahinta = hinta / pinta
    return pintahinta

halkaisija = float(input("Anna ensimmäisen pitsan halkaisija: "))
hinta = float(input("Anna ensimmäisen pitsan hinta euroina: "))
halkaisija2 = float(input("Anna toisen pitsan halkaisija: "))
hinta2 = float(input("Anna toisen pitsan hinta euroina: "))

ekapitsa = laskehinta(halkaisija, hinta)
tokapitsa = laskehinta(halkaisija2, hinta2)

if ekapitsa > tokapitsa:
    print("Toinen pitsa on halvempaa")
else:
    print("Ensimmäinen pitsa on halvempaa")