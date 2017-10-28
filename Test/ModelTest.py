import unittest
from model import Menu, AvailableIngredients, Constants
from model.Menu import Ingredient, Pizza
from model.Request import RequireTagConstraint, RejectTagConstraint


class TestTags(unittest.TestCase):
    def setUp(self):
        self.cheese_name = "Cheese"
        self.tomato_name = "Tomato"
        self.ham_name = "Ham"
        self.lactose_tag = "Lactose"
        self.meat_tag = "Meat"
        self.spicy_tag = "Spicy"
        self.napolitan_name = "Napolitan"
        self.pizza_size = 3

        self.cheese = Menu.Ingredient(self.cheese_name).add_tag(self.lactose_tag)
        self.tomato = Menu.Ingredient(self.tomato_name)
        self.ham = Menu.Ingredient(self.ham_name).add_tag(self.meat_tag)

        self.pizza = Pizza(self.napolitan_name, self.pizza_size).add_ingredient(self.cheese).add_ingredient(
            self.tomato).add_ingredient(self.ham)

        self.reject_lactose = RejectTagConstraint(self.lactose_tag)
        self.require_meat = RequireTagConstraint(self.meat_tag)
        self.reject_meat = RejectTagConstraint(self.meat_tag)

    def test_ingredient_tags(self):
        self.assertTrue(self.cheese.has_tag(self.lactose_tag))
        self.assertFalse(self.tomato.has_tag(self.lactose_tag))
        self.assertFalse(self.tomato.has_tag(self.meat_tag))
        self.assertFalse(self.ham.has_tag(self.lactose_tag))
        self.assertTrue(self.ham.has_tag(self.meat_tag))

    def test_pizza_tags(self):
        self.assertTrue(self.pizza.has_tag(self.lactose_tag))
        self.assertTrue(self.pizza.has_tag(self.meat_tag))
        self.assertFalse(self.pizza.has_tag(self.spicy_tag))

    def test_constraint(self):
        self.assertTrue(self.require_meat.eval(self.pizza))
        self.assertFalse(self.reject_lactose.eval(self.pizza))
        self.assertFalse(self.reject_meat.eval(self.pizza))


if __name__ == '__main__':
    unittest.main()
