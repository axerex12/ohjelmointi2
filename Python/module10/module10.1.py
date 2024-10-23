class HISSI:

    def __init__(self, alin, ylin):
        self.nykykerros = 1
        self.alin=alin
        self.ylin=ylin

    def kerros_alas(self):
        self.nykykerros -= 1

    def kerros_ylös(self):
        self.nykykerros += 1

    def siirry_kerrokseen(self,kerros):
        if self.nykykerros > kerros:
            while self.nykykerros != kerros:
                print(f"Kerros on: {self.nykykerros}")
                self.kerros_alas()
        elif self.nykykerros < kerros:
            while self.nykykerros < kerros:
                print(f"Kerros on: {self.nykykerros}")
                self.kerros_ylös()


h = HISSI(1,6)
h.siirry_kerrokseen(5)

print(f"Nykyinen kerros on: {h.nykykerros}")

h.siirry_kerrokseen(1)

print(f"Nykyinen kerros on: {h.nykykerros}")