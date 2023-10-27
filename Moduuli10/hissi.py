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