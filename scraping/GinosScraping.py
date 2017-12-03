import re  # regex

import requests  # html
from bs4 import BeautifulSoup  # sopita


# realiza la petición html y lo transforma en sopita
def get_soup(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, "html.parser")


# se usa una regex para ver si el titulo parte con un numero seguido de un punto
def is_pizza(titulo):
    return re.match("[0-9]+\.", titulo)


# OMG TESTING
assert is_pizza("16. Salame")
assert is_pizza("Promociones disponibles con todas las pizzas excepto la 20.") is None


# obtiene el menu de pizzas y lo devuelve en un arreglo
def get_ginos_menu():
    url = 'http://www.ginospizza.cl/pizzas'
    soup = get_soup(url)

    # div donde esta menu de ginos
    listado = soup.find("div", id="listado")

    # los titulos son <h1>, pero hay otras cosas ademas de pizzas
    titulos = listado.find_all("h1")
    # ingredientes siempre en <p>
    ingredientes = listado.find_all("p")
    # precios siempre en <h2>, pero hay más precios que pizzas (bebidas y otros)
    precios = listado.find_all("h2")

    pizzas = []

    # solo las pizzas tienen  ingredientes
    # el primer titulo es el de las promociones asi que se desplaza en 1
    for i in range(len(ingredientes)):
        # TODO guardar en estructura boni
        pizza = [titulos[i + 1].get_text(),
                 ingredientes[i].get_text(),
                 precios[i].get_text()]
        pizzas.append(pizza)

    return pizzas


if __name__ == '__main__':
    menu = get_ginos_menu()
    for item in menu:
        print(item)
