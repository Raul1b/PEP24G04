class Masina:
    def __init__(self, marca: str, usi: int, culoare: str, an:
    int, pret: float):
        self.marca = marca
        self.usi = usi
        self.culoare = culoare
        self.an = an
        self.__pret = pret

    def __add__(self, other):
        return Masina('', 0, '', 0, self.get_pret() + other.get_pret())

    def get_pret(self):
        return self.__pret


masina1 = Masina("Audi", 4, "gri", 2006, 3400)
masina2 = Masina("BMW", 2, "maro", 2007, 4788.60)
masina3 = Masina("Volvo", 4, "gri", 2017, 27000)
masina4 = Masina("Audi", 4, "negru", 2013, 10200)
masina5 = Masina("Audi", 2, "gri", 2005, 3400)
masina6 = Masina("BMW", 4, "negru", 2017, 22000)
masina7 = Masina("Volvo", 4, "gri", 2017, 27000)
masini = [masina7, masina6, masina5, masina4, masina3, masina1, masina2]

# sum(masini)/len(masini)
# masina7 + masina6 + masina5 + masina4 + masina3 + masina1 + masina2

print(sum(masini, Masina('', 0, '', 0, 0.0)).get_pret() / len(masini))

# pret_t = sum(m.get_pret() for m in masini)
# print(pret_t / len(masini))

nr_bmw = len(list(filter(lambda m: m.marca == "BMW", masini)))
print(nr_bmw)

car_audi = list(filter(lambda masina: masina.marca == "Audi", masini))
print(sum(map(lambda masina: masina.an, car_audi)) / len(list(car_audi)))

marca_cautata = input("Introduceti marca de masina cautata:")
nr_masini = len(list(filter(lambda m: m.marca == marca_cautata, masini)))
print(nr_masini)