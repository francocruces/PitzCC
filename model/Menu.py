import abc


class MenuElement(metaclass=abc.ABCMeta):
    """
    A menu element, represents anything the store offers.
    Has is_xxxx() methods for testing.
    """

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def is_food(self):
        return False

    def is_drink(self):
        return False

    def is_pizza(self):
        return False

    @abc.abstractmethod
    def has_tag(self, tag):
        pass


class Food(MenuElement):
    """
    Food. Menu element.
    """

    def __init__(self, name):
        super(Food, self).__init__(name)

    @abc.abstractmethod
    def has_tag(self, tag):
        pass

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

    def has_ingredient_name(self, ing_name):
        for i in self.ingredients:
            if i.get_name() == ing_name:
                return True
        return False

    def get_ingredients(self):
        return self.ingredients


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

    def get_name(self):
        return self.name

    def get_tags(self):
        return self.tags


class Drink(MenuElement):
    """
    Drink. Menu element.
    """

    def __init__(self, name, size):
        super(Drink, self).__init__(name)
        self.size = size

    def get_size(self):
        return self.size

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

    def get_items(self):
        return self.items

    def get_price(self):
        return self.price

    def has_tag(self, tag):
        for e in self.items:
            if e.has_tag(tag):
                return True
        return False

    def has_ingredient_name(self, ing_name):
        for e in self.items:
            if e.has_ingredient_name(ing_name):
                return True
        return False
