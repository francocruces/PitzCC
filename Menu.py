
class MenuElement:
    """
    A menu element, represents anything the store offers.
    """
    def __init__(self, name):
        self.name = name

    def is_food(self):
        return self.__class__ == Food

    def is_drink(self):
        return self.__class__ == Drink

    def is_pizza(self):
        return self.__class__ == Pizza

    def is_ingredient(self):
        return self.__class__ == Ingredient


class Food(MenuElement):
    """
    Food. Menu element.
    """
    def __init__(self, name):
        super(Food, self).__init__(name)


class Pizza(Food):
    """
    A pizza. It's a Food MenuElement. Has ingredients and a size.
    """
    def __init__(self, name, size):
        super(Pizza, self).__init__(name)
        self.size = size
        self.ingredients = []

    def add_ingredient(self, ingredient):
        """
        Add given ingredient to the pizza.
        :param ingredient: Ingredient object to add
        :type ingredient: Ingredient
        """
        self.ingredients.append(ingredient)


class Ingredient:
    """
    An ingredient. Currently only used for pizzas, but could be used in any other type of food.
    """
    def __init__(self, name):
        self.name = name
        self.tags = []

    def has_tag(self, tag):
        self.tags.__contains__(tag)

    def add_tag(self, tag):
        self.tags.append(tag)
        return self.tags


class Drink(MenuElement):
    """
    Drink. Menu element.
    """
    def __init__(self, name, size):
        super(Drink, self).__init__(name)
        self.size = size


class PricedElement:
    """
    A set of MenuElements with an associated price.
    """
    def __init__(self, menu_elements, price):
        """
        Constructor.
        :param menu_elements: Array of MenuElement
        :param price: Price for given set of elements
        :type price: int
        """
        self.items = menu_elements
        self.price = price
