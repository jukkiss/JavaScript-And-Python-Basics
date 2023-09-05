
def listaMuunnin(parittomat):
    parilliset = []
    for x in parittomat:
        if x % 2 == 0:
            parilliset.append(x)
    return parilliset

parittomat = [1,2,3,4,5,6,7,8,9]

print(parittomat)
print(listaMuunnin(parittomat))
