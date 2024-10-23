import random
class auto:

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


autot = []

for i in range(1,11):
    rekkari = f"ABC-{i}"
    maxnopeus = random.randint(100, 200)
    auuto = auto(rekkari, maxnopeus)
    autot.append(auuto)

raceon = True
while raceon:
    for auto in autot:
        randkiihd = random.randint(-10, 15)
        auto.kiihdytä(randkiihd)
        auto.kulje(1)
    for auto in autot:
        if auto.kuljettumatka > 10000:
            print(f"Auto {auto.rekis} on saavuttanut yli 10 000 km ja race on over")
            raceon = False
            break

print("\nKilpailun päätyttyä autojen tiedot ovat seuraavat:\n")
print(f"{'Rekkari ':<8}{'Huippunopeus':<15}{'Nykyinen nopeus ':<15}{'Kuljettu matka':<15}")
print("-" * 60)


for auto in autot:
    print(f"{auto.rekis:<8}{auto.huippunopeus:<15}{auto.nopeus:<15}{auto.kuljettumatka:<15}")