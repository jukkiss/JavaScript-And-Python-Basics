class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0
    def kiihdytä(self, muutos):
        uusin = self.nopeus + muutos
        if uusin < 0:
            self.nopeus = 0
        elif uusin > self.huippunopeus:
            self.nopeus = self.huippunopeus
        else:
            self.nopeus = uusin

    def kulje(self, tuntimäärä):
        matkamäärä = self.nopeus * tuntimäärä
        self.matka += matkamäärä