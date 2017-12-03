import abc
from ..Menu import MenuElement
from ..PricedSet import PricedSet


class MenuVisitor(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def visit_menu_element(self, element):
        pass

    @abc.abstractmethod
    def visit_priced_set(self, set):
        pass

    @abc.abstractmethod
    def display(self):
        pass


class PizzaNumberVisitor(MenuVisitor):
    """
    Stores the number of pizzas from a set of elements
    """

    def __init__(self):
        self.pizzaNum = 0

    def visit_menu_element(self, element: MenuElement) -> None:
        """
        Adds one to the pizzaNum counter if the element is pizza
        :param element: the Menu element
        """

        if element.is_pizza():
            self.pizzaNum += 1

    def visit_priced_set(self, aPricedSet: PricedSet) -> None:
        """
        Visits a priced set to see how many pizzas does it have
        :param aPricedSet: the priced set visited
        """
        pass

    def display(self) -> int:
        """
        Returns the number of pizzas of the elements visited
        :return: the number of pizzas of the elements visited
        """
        return self.pizzaNum
