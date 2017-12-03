import abc

from model.Size import Size


class MenuElement(metaclass=abc.ABCMeta):
    """
    A menu element, represents anything the store offers.
    Has is_xxxx() methods for testing.
    """

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name

    def is_food(self):
        return False

    def is_drink(self):
        return False

    def is_pizza(self):
        return False

    def accept_visitor(self, visitor):
        visitor.visit_menu_element(self)

    @abc.abstractmethod
    def has_tag(self, tag):
        pass


class ElementWithIngredients:
    def __init__(self):
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

    def has_ingredient_name(self, ing_name):
        for i in self.ingredients:
            if i.get_name() == ing_name:
                return True
        return False

    def get_ingredients(self):
        return self.ingredients


class SizedElement:
    def __init__(self, size):
        """
        Constructor.
        :param size: Size object for this element
        :type size: Size
        """
        self.size = size

    def get_size(self):
        return self.size.get_nominal_size()

    def get_satiety_index(self):
        return self.size.get_real_size()

    def get_size_object(self):
        return self.size


class Food(MenuElement):
    """
    Food. Menu element.
    """

    def __init__(self, name, price):
        super(Food, self).__init__(name, price)

    @abc.abstractmethod
    def has_tag(self, tag):
        pass

    def is_food(self):
        return True


class Pizza(ElementWithIngredients, Food, SizedElement):
    """
    A pizza. It's a Food MenuElement and an ElementWithIngredients. Has ingredients and a size.
    """

    def __init__(self, name, size, price):
        Food.__init__(self, name, price)
        ElementWithIngredients.__init__(self)
        SizedElement.__init__(self, size)

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

    def get_name(self):
        return self.name

    def get_tags(self):
        return self.tags


class Drink(MenuElement, SizedElement):
    """
    Drink. Menu element.
    """

    def __init__(self, name, size, price):
        MenuElement.__init__(self, name, price)
        SizedElement.__init__(self, size)

    def has_tag(self, tag):
        return False

    def is_drink(self):
        return True
