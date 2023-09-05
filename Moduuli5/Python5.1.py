import random

nopat = int(input("Anna arpakuutioiden määrä: "))
yhteisluku = 0

for x in range(nopat):
    yhteisluku += random.randint(1, 6)

print(yhteisluku)