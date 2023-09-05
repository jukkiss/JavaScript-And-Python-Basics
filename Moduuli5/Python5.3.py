import math
inputti = int(input("Anna kokonaisluku: "))

onAlkuluku = True

for x in range(2, inputti):
    if inputti % x == 0:
        onAlkuluku = False

if onAlkuluku == True:
    print("Luku on alkuluku.")
else:
    print("Luku ei ole alkuluku.")