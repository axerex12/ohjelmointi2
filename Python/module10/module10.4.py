import random

class Kilpailu:
    def __init__(self, nimi, pituuskm, osallistuja_lista):
        self.nimi = nimi
        self.pituuskm = pituuskm
        self.osallistuja_lista = osallistuja_lista

    def tunti_kuluu(self):
        for auto in self.osallistuja_lista:
            randkiihd = random.randint(-10, 15)
            auto.kiihdytä(randkiihd)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"{'Rekisteri':<10}{'Huippunopeus':<15}{'Nopeus':<15}{'Kuljettu matka':<15}")
        print("="*55)
        for auto in self.osallistuja_lista:
            print(f"{auto.rekis:<10}{auto.huippunopeus:<15}{auto.nopeus:<15}{auto.kuljettumatka:<15}")

    def kilpailu_ohi(self):
        for auto in self.osallistuja_lista:
            if auto.kuljettumatka >= self.pituuskm:
                print(f"Auto {auto.rekis} on saavuttanut maalin!")
                return True
        return False


class Auto:

    def __init__(self, rekis, huippunopeus):
        self.rekis = rekis
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettumatka = 0

    def kiihdytä(self, nopeuden_muutos):
        if self.nopeus + nopeuden_muutos > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus + nopeuden_muutos < 0:
            self.nopeus = 0
        else:
            self.nopeus += nopeuden_muutos

    def kulje(self, tuntimäärä):
        self.kuljettumatka += self.nopeus * tuntimäärä



autot = []
for i in range(1, 11):
    rekkari = f"ABC-{i}"
    maxnopeus = random.randint(100, 200)
    autot.append(Auto(rekkari, maxnopeus))


kisa = Kilpailu("Suuri romuralli", 8000, autot)


tunti = 0
while not kisa.kilpailu_ohi():
    kisa.tunti_kuluu()
    tunti += 1
    if tunti % 10 == 0:
        kisa.tulosta_tilanne()

print(f"Kilpailu päättyi {tunti} tunnin jälkeen.")
kisa.tulosta_tilanne()
