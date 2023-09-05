import random as r


def heitto():
    noppa = r.randint(1, 6)
    return noppa

while True:
    heitot = heitto()
    print(heitot)
    if heitot == 6:
        break




