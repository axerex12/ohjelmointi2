class auto:
    pass
    def __init__(self, rekis, huippunopeus):
        self.rekis = rekis
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettumatka = 0

    def kiihdytä(self, nopeuden_muutos):
        if self.nopeus + nopeuden_muutos > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus + nopeuden_muutos < 0:
            self.nopeus =0
        else:
            self.nopeus += nopeuden_muutos
    def kulje(self, tuntimäärä):
        self.kuljettumatka += self.nopeus * tuntimäärä




autoh = auto("ABC-123", 142)

autoh.kiihdytä(30)
autoh.kulje(1)
autoh.kiihdytä(70)
autoh.kiihdytä(50)
print(autoh.nopeus)
autoh.kiihdytä(-200)
print(autoh.nopeus)
print(autoh.kuljettumatka)
print(f"Auton rekkari: {autoh.rekis} auton huippu nopeus: {autoh.huippunopeus}km/h kuljettu matka on {autoh.kuljettumatka}km auton nopeus on {autoh.nopeus}km/h")