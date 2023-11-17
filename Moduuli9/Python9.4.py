import random
from auto import Auto

autot = []

for i in range(1, 11):
    rekisteri = "ABC-" + str(i)
    maksimi = random.randint(100,200)
    kilpa_auto = Auto(rekisteri, maksimi)
    autot.append(kilpa_auto)

for kilpa_auto in autot:
    kilpa_auto.kiihdytä(80)

jatketaan = True
kilpa_aika = 0

while jatketaan:
    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdytä(muutos)
        auto.kulje(1)
        if auto.matka >= 10000:
            jatketaan = False

    kilpa_aika += 1

print(F"Kilpailun kesto oli {kilpa_aika}h.")

def lajittelija(kilpa_auto):
    return kilpa_auto.matka

autot.sort(reverse=True, key=lajittelija)

print(f"Rekkari \tMax\tnopeus\tMatka")
for kilpa_auto in autot:
    print(f"{kilpa_auto.rekisteritunnus} \t{kilpa_auto.huippunopeus}"
          f"\t{kilpa_auto.nopeus} \t{kilpa_auto.matka} ")


