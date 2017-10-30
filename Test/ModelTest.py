import math
import unittest

from model.Menu import Pizza, PricedSet, Ingredient
from model.Request import RequireTagConstraint, RejectTagConstraint, Request
from model.Size import DiameterSize


class TestTags(unittest.TestCase):
    def setUp(self):
        self.cheese_name = "Cheese"
        self.tomato_name = "Tomato"
        self.ham_name = "Ham"
        self.lactose_tag = "Lactose"
        self.meat_tag = "Meat"
        self.spicy_tag = "Spicy"
        self.napolitan_name = "Napolitan"
        self.pizza_size = DiameterSize(20)
        self.pizza_price = 4000

        self.cheese = Ingredient(self.cheese_name).add_tag(self.lactose_tag)
        self.tomato = Ingredient(self.tomato_name)
        self.ham = Ingredient(self.ham_name).add_tag(self.meat_tag)

        self.pizza = Pizza(self.napolitan_name, self.pizza_size).add_ingredient(self.cheese).add_ingredient(
            self.tomato).add_ingredient(self.ham)

        self.reject_lactose = RejectTagConstraint(self.lactose_tag)
        self.require_meat = RequireTagConstraint(self.meat_tag)
        self.reject_meat = RejectTagConstraint(self.meat_tag)

        self.request1 = Request().add_constraint(self.require_meat)
        self.request2 = Request().add_constraint(self.require_meat).add_constraint(self.reject_lactose)

        self.priced = PricedSet([self.pizza], self.pizza_price)

    def test_ingredient_instance(self):
        self.assertEqual(self.cheese.get_name(), "Cheese")
        self.assertEqual(self.tomato.get_name(), "Tomato")
        self.assertEqual(self.ham.get_name(), "Ham")

        self.assertEqual(self.cheese.get_tags(), ["Lactose"])
        self.assertEqual(self.tomato.get_tags(), [])
        self.assertEqual(self.ham.get_tags(), ["Meat"])

    def test_pizza_instance(self):
        self.assertEqual(self.pizza.get_name(), "Napolitan")
        self.assertTrue(self.pizza.is_food())
        self.assertTrue(self.pizza.is_pizza())
        self.assertFalse(self.pizza.is_drink())
        self.assertEqual(self.pizza.get_size(), 20)
        self.assertEqual(self.pizza.get_satiety_index(), 100 * math.pi)

        self.assertEqual(self.pizza.get_ingredients(), [self.cheese, self.tomato, self.ham])
        self.assertTrue(self.pizza.has_ingredient_name("Cheese"))
        self.assertTrue(self.pizza.has_ingredient_name("Tomato"))
        self.assertTrue(self.pizza.has_ingredient_name("Ham"))
        self.assertFalse(self.pizza.has_ingredient_name("Corn"))

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

    def test_request_eval(self):
        self.assertTrue(self.request1.eval_item(self.pizza))
        self.assertFalse(self.request2.eval_item(self.pizza))

    def test_request_instance(self):
        self.assertEqual(self.priced.get_items(), [self.pizza])
        self.assertEqual(self.priced.get_price(), 4000)
        self.assertTrue(self.priced.has_tag("Lactose"))
        self.assertFalse(self.priced.has_tag("Spicy"))
        self.assertTrue(self.priced.has_ingredient_name("Cheese"))
        self.assertFalse(self.priced.has_ingredient_name("Corn"))


if __name__ == '__main__':
    unittest.main()
