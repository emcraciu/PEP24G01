class Categorii:
    def __init__(self, nume, pret, stoc):
        self.nume = nume
        self.pret = pret
        self.stoc = stoc


class Haine(Categorii):
    pass


class Accesorii(Categorii):
    pass


class Incaltaminte(Categorii):
    pass


if __name__ == "__main__":
    tricouri = Haine("tricou", 20, 35)
    print(tricouri.__class__.__name__)
    print(type(tricouri))
