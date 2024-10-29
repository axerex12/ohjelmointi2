import random

class Kilpailu:
    def __init__(self, nimi, pituuskm, osallistuja_lista, kesto):
        self.nimi = nimi
        self.pituuskm = pituuskm
        self.osallistuja_lista = osallistuja_lista
        self.kesto = kesto
        self.kulunut = 0

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
                print(f"Auto {auto.rekis} on saavuttanut maalin! tai aika kului loppuun!")
                return True
            elif self.kesto <= self.kulunut:
                print(f"Aika Loppui!")
                return True
        self.kulunut +=1
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

class sähköauto(Auto):
    def __init__(self, rekis, huippunopeus, kapasiteetti):
        self.kapasiteetti = kapasiteetti
        super(). __init__(rekis, huippunopeus)

class bensaauto(Auto):
    def __init__(self,rekis, huippunopeus, tankki):
        self.tankki = tankki
        super().__init__(rekis, huippunopeus)


autot = []

autot.append(bensaauto("ABC-123", 165, 32.3))
autot.append(sähköauto("ABC-15", 180, 52.5))


kisa = Kilpailu("Suuri romuralli", 8000, autot, 3)



while not kisa.kilpailu_ohi():
    kisa.tunti_kuluu()
    kisa.tulosta_tilanne()

