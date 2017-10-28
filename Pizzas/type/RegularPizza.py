from Pizzas.type.IPizza import IPizza

class RegularPizza(IPizza):

    def __init__(self, name, price, size, ingredients):
        self.name = name
        self.price = price
        self.size = size
        self.ingredients = ingredients

    def getPrice(self):
        return self.price

    def getName(self):
        return self.name

    def getSize(self):
        return  self.size

    def getIngredients(self):
        return self.ingredients

    def hasIngredient(self, anIngredient):
        for ingredient in self.ingredients:
            if (anIngredient == ingredient):
                return True
        return False



