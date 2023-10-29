from julkaisu import Kirja, Lehti


julkaisut = []

julkaisut.append(Lehti("Aku Ankka","Aki Hyyppä"))
julkaisut.append(Kirja("Hytti nro 6", "Rosa Liksom", 200))

for j in julkaisut:
    j.tulosta_tiedot()