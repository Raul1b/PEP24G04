MENU = """
Meniu:
1. Vizualizare stoc
2. Adaugare produs
3. Stergere produs
4. Iesire
"""


def add_stoc():
    products = input("Adauga produse (produs, pret, stoc): ")
    product, price, stock = products.split(',')
    price = int(price)
    stock = int(stock)

    if product in STOCK:
        data = STOCK[product]
        data.update({price: data.get(price, 0) + stock})
    else:
        STOCK.update({product: {price: stock}})


def get_stoc():
    print(STOCK)


ACTIONS = {'1': get_stoc, '2': add_stoc, '3': quit, '4': quit, }
STOCK = {}

while True:
    print(MENU)
    selection = input(':')
    assert selection in ACTIONS
    f = ACTIONS[selection]
    f()
