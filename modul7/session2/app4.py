class Angajat:
    def __init__(self, nume, salar):
        self.nume = nume
        self.salar = salar

    def __str__(self):
        return f"Nume: {self.nume}, Salar: {self.salar}"


class Angajati:
    lista_angajati = []

    def adauga_angajati(self, *args):
        self.lista_angajati.extend(list(args))

    def detalii_angajat(self):
        for angajat in self.lista_angajati:
            print(angajat)


angajati = Angajati()
angajati.adauga_angajati(Angajat("George", "1000"), Angajat("Alex", "2000"))
angajati.detalii_angajat()
