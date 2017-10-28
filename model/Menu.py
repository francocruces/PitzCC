import abc


class MenuElement:
    """
    A menu element, represents anything the store offers.
    Has is_xxxx() methods for testing.
    """

    def __init__(self, name):
        self.name = name

    def is_food(self):
        return False

    def is_drink(self):
        return False

    def is_pizza(self):
        return False

    @abc.abstractmethod
    def has_tag(self, tag):
        return False


class Food(MenuElement):
    """
    Food. Menu element.
    """

    def __init__(self, name):
        super(Food, self).__init__(name)

    @abc.abstractmethod
    def has_tag(self, tag):
        return False

    def is_food(self):
        return True


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
        :return self for chaining
        """
        self.ingredients.append(ingredient)
        return self

    def has_tag(self, tag):
        for i in self.ingredients:
            if i.has_tag(tag):
                return True
        return False

    def is_pizza(self):
        return True


class Ingredient:
    """
    An ingredient. Currently only used for pizzas, but could be used in any other type of food.
    """

    def __init__(self, name):
        self.name = name
        self.tags = []

    def has_tag(self, tag):
        return self.tags.__contains__(tag)

    def add_tag(self, tag):
        """
        Add a tag to this ingredient.
        :param tag: A tag
        :return: self for chaining
        """
        self.tags.append(tag)
        return self
    

class Drink(MenuElement):
    """
    Drink. Menu element.
    """

    def __init__(self, name, size):
        super(Drink, self).__init__(name)
        self.size = size

    def has_tag(self, tag):
        return False

    def is_drink(self):
        return True


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
