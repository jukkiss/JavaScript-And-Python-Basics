import random

yksi = random.randint(0, 9)
kaksi = random.randint(0, 9)
kolme = random.randint(0, 9)

nelja = random.randint(1, 6)
viisi = random.randint(1, 6)
kuusi = random.randint(1, 6)
seitseman = random.randint(1, 6)

kaikki = f"Lukkosi koodi on {yksi}{kaksi}{kolme}, toisen lukon koodisi on {nelja}{viisi}{kuusi}{seitseman}."

print(kaikki)
