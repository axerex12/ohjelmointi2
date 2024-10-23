class TALO:
    def __init__(self, ylink, alink, hissimäärä):
        self.ylink = ylink
        self.alink = alink
        self.hissimäärä = hissimäärä
        self.hissit=[]
        i = 0
        while i != hissimäärä:
            h = HISSI(alink,ylink)
            self.hissit.append(h)
            i+=1

    def aja_hissiä(self, hnumero, kohde):
        hissi = self.hissit[-1+hnumero]
        hissi.siirry_kerrokseen(kohde)
        print(f"Hissi numero {hnumero} on kerroksessa {hissi.nykykerros}")





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


talo = TALO(6, 1, 4)

talo.aja_hissiä(4,6)


