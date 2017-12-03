class PricedSet:
    """
    A set of MenuElements with an associated price.
    """

    def __init__(self, menu_elements, price):
        """
        Constructor.
        :param menu_elements: Array of MenuElement
        :type menu_elements: list
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

    def calc_applied_discount(self):
        regular_price = 0
        for e in self.items:
            regular_price += e.get_price()
        return regular_price - self.price
