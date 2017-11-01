from model.PricedSet import PricedSet


class SpecialOffer:
    def __init__(self, price):
        self.price = price
        self.offer_placeholders = []

    def add_placeholder(self, placeholder):
        self.offer_placeholders.append(placeholder)
        return self

    def add_constraint_to_all(self, constraint):
        for placeholder in self.offer_placeholders:
            placeholder.add_constraint(constraint)

    def apply(self, menu_elements):
        """
        Applies SpecialOffer to given set and returns a PricedSet containing only matching elements.
        :param menu_elements: Array of menu_elements
        :type menu_elements: list
        :return: A pricedSet with matching elements
        """
        given_elements = menu_elements.copy()
        for placeholder in self.offer_placeholders:
            for element in given_elements:
                if placeholder.accept(element):
                    given_elements.remove(element)
        return self.to_priced_set()

    def to_priced_set(self):
        """
        Converts self into a PricedElement with its placeholders.
        :return: PricedSet with elements from placeholders. None if any placeholder isn't set
        :rtype PricedSet
        """
        elements = []
        for placeholder in self.offer_placeholders:
            if not placeholder.is_set():
                return None
            elements.append(placeholder.get_element())
        return PricedSet(elements, self.price)


class OfferPlaceholder:
    def __init__(self):
        self.constraints = []
        self.menu_element = None

    def add_constraint(self, constraint):
        self.constraints.append(constraint)
        return self

    def accept(self, item):
        # If it's set, do not accept. Should not happen.
        if self.is_set():
            return False
        # Check all constraints
        for c in self.constraints:
            if not c.accept(item):
                return False
        self.menu_element = item
        return True

    def set_element(self, element):
        self.menu_element = element

    def is_set(self):
        return self.menu_element is not None

    def get_element(self):
        return self.menu_element
