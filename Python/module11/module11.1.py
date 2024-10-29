class JULKAISU:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"Julkaisun nimi: {self.nimi}")



class kirja(JULKAISU):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
        super().__init__(nimi)
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"kirjoittaja: {self.kirjoittaja} {self.sivumäärä} sivua")




class lehti(JULKAISU):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimitaja = päätoimittaja
        self.nimi = nimi
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"lehden päätoimittaja: {self.päätoimitaja}")

julkaisut = []
julkaisut.append(kirja("Hytti n.o6", "Rosa Liksom", 200))
julkaisut.append(lehti("Aku Ankka", "Aki Hyppää"))
for j in julkaisut:
    j.tulosta_tiedot()