class Julkaisu:

    def __init__(self, input_nimi):
        self.nimi = input_nimi

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}")

class Kirja(Julkaisu):
    def __init__(self,input_nimi, input_kirjoittaja, input_sivumäärä):
        self.kirjoittaja = input_kirjoittaja
        self.sivumäärä = input_sivumäärä
        super().__init__(input_nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kirjoittaja {self.kirjoittaja}. Sivumäärä {self.sivumäärä}.")

class Lehti(Julkaisu):

    def __init__(self, input_nimi, input_päätoimittaja):
        self.päätoimittaja = input_päätoimittaja
        super().__init__(input_nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Päätoimittaja {self.päätoimittaja}")

