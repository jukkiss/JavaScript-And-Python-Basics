



def litramuunnin(gallonat):
    litrat = gallonat * 3.785
    print(litrat)

while True:
    gallonat = float(input("Anna gallonat: "))
    if gallonat < 0:
        break
    litramuunnin(gallonat)

