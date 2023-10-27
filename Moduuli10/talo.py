class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissin_kerros = alin_kerros

    def siirry_kerrokseen(self, meno_kerros):
        while self.hissin_kerros != meno_kerros:
            if self.hissin_kerros < meno_kerros:
                self.kerros_ylös()
            else:
                self.kerros_alas()

    def kerros_ylös(self):
        if self.hissin_kerros < self.ylin_kerros:
            self.hissin_kerros +=1
        print(f"Hissin kerros on {self.hissin_kerros}")

    def kerros_alas(self):
        if self.hissin_kerros > self.alin_kerros:
            self.hissin_kerros -= 1
        print(f"Hissin kerros on {self.hissin_kerros}")

class Talo:
    def __init__(self,alin, ylin, hissien_lkm):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []

        for i in range(hissien_lkm):
            hissi = Hissi(self.alin, self.ylin)
            self.hissit.append(hissi)


    def aja_hissiä(self, hissin_nro, kohdekerros):
        hissi = self.hissit[hissin_nro -1]
        hissi.siirry_kerrokseen(kohdekerros)
        print(f"{hissin_nro} on nyt kerroksessa {kohdekerros}")

    def kerro_hissien_sijainnit(self):
        print("- Talon hissien sijainnit -")
        for i in range(len(self.hissit)):
            print(f"hissi {i+1} on kerroksessa {self.hissit[i].hissin_kerros}")
        return

    def palohälytys(self):
        pass


