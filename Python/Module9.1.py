class auto:
    pass
    def __init__(self, rekis, huippunopeus):
        self.rekis = rekis
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettumatka = 0

autoh = auto("ABC-123", "142km/h")

print(f"Auton rekkari: {autoh.rekis} auton huppu nopeus: {autoh.huippunopeus} ja {autoh.kuljettumatka} ja {autoh.nopeus}")