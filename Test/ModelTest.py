import math
import unittest

from model.Menu import Pizza, Ingredient, Drink
from model.PricedSet import PricedSet
from model.Constraint import RequireTagConstraint, RejectTagConstraint
from model.Request import Request
from model.SpecialOffer import SpecialOffer, OfferPlaceholder
from model.Size import DiameterSize, LiquidSize
from model.Constraint import IsDrinkConstraint, IsFoodConstraint, IsPizzaConstraint, SizeConstraint


class TestTags(unittest.TestCase):
    def setUp(self):
        pass

    def set_requests(self):
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

        self.pizza = Pizza(self.napolitan_name, self.pizza_size, 1000).add_ingredient(self.cheese).add_ingredient(
            self.tomato).add_ingredient(self.ham)

        self.reject_lactose = RejectTagConstraint(self.lactose_tag)
        self.require_meat = RequireTagConstraint(self.meat_tag)
        self.reject_meat = RejectTagConstraint(self.meat_tag)

        self.request1 = Request().add_constraint(self.require_meat)
        self.request2 = Request().add_constraint(self.require_meat).add_constraint(self.reject_lactose)

        self.priced = PricedSet([self.pizza], self.pizza_price)

    def test_ingredient_instance(self):
        self.set_requests()
        self.assertEqual(self.cheese.get_name(), "Cheese")
        self.assertEqual(self.tomato.get_name(), "Tomato")
        self.assertEqual(self.ham.get_name(), "Ham")

        self.assertEqual(self.cheese.get_tags(), ["Lactose"])
        self.assertEqual(self.tomato.get_tags(), [])
        self.assertEqual(self.ham.get_tags(), ["Meat"])

    def test_pizza_instance(self):
        self.set_requests()
        self.assertEqual(self.pizza.get_name(), "Napolitan")
        self.assertTrue(self.pizza.is_food())
        self.assertTrue(self.pizza.is_pizza())
        self.assertFalse(self.pizza.is_drink())
        self.assertEqual(self.pizza.get_size(), 20)
        self.assertEqual(self.pizza.get_satiety_index(), 100 * math.pi)
        self.assertEqual(self.pizza.get_price(), 1000)

        self.assertEqual(self.pizza.get_ingredients(), [self.cheese, self.tomato, self.ham])
        self.assertTrue(self.pizza.has_ingredient_name("Cheese"))
        self.assertTrue(self.pizza.has_ingredient_name("Tomato"))
        self.assertTrue(self.pizza.has_ingredient_name("Ham"))
        self.assertFalse(self.pizza.has_ingredient_name("Corn"))

    def test_ingredient_tags(self):
        self.set_requests()
        self.assertTrue(self.cheese.has_tag(self.lactose_tag))
        self.assertFalse(self.tomato.has_tag(self.lactose_tag))
        self.assertFalse(self.tomato.has_tag(self.meat_tag))
        self.assertFalse(self.ham.has_tag(self.lactose_tag))
        self.assertTrue(self.ham.has_tag(self.meat_tag))

    def test_pizza_tags(self):
        self.set_requests()
        self.assertTrue(self.pizza.has_tag(self.lactose_tag))
        self.assertTrue(self.pizza.has_tag(self.meat_tag))
        self.assertFalse(self.pizza.has_tag(self.spicy_tag))

    def test_constraint(self):
        self.set_requests()
        self.assertTrue(self.require_meat.accept(self.pizza))
        self.assertFalse(self.reject_lactose.accept(self.pizza))
        self.assertFalse(self.reject_meat.accept(self.pizza))

    def test_request_eval(self):
        self.set_requests()
        self.assertTrue(self.request1.eval_item(self.pizza))
        self.assertFalse(self.request2.eval_item(self.pizza))

    def test_request_instance(self):
        self.set_requests()
        self.assertEqual(self.priced.get_items(), [self.pizza])
        self.assertEqual(self.priced.get_price(), 4000)
        self.assertTrue(self.priced.has_tag("Lactose"))
        self.assertFalse(self.priced.has_tag("Spicy"))
        self.assertTrue(self.priced.has_ingredient_name("Cheese"))
        self.assertFalse(self.priced.has_ingredient_name("Corn"))

    def set_placeholders(self):
        self.ph1 = OfferPlaceholder().add_constraint(RequireTagConstraint("Meat"))
        self.ph2 = OfferPlaceholder().add_constraint(RejectTagConstraint("Meat"))
        self.offer = SpecialOffer(1000).add_placeholder(self.ph1).add_placeholder(self.ph2)

        self.veg_pizza = Pizza("Veggie", DiameterSize(10), 1000).add_ingredient(self.tomato)
        self.veg_pizza2 = Pizza("Veggie2", DiameterSize(10), 1000).add_ingredient(self.tomato)
        self.meat_pizza = Pizza("Meaty", DiameterSize(10), 1000).add_ingredient(self.ham)

    def test_special_offer(self):
        self.set_requests()
        self.set_placeholders()
        pack = self.offer.apply([self.veg_pizza, self.veg_pizza2, self.meat_pizza])
        self.assertIsNotNone(pack)
        self.assertEqual(pack.get_price(), 1000)
        self.assertTrue(pack.has_tag("Meat"))
        self.assertTrue(pack.has_ingredient_name("Ham"))
        self.assertTrue(pack.has_ingredient_name("Tomato"))
        self.assertTrue(self.veg_pizza in pack.get_items())
        self.assertTrue(self.meat_pizza in pack.get_items())
        self.assertFalse(self.veg_pizza2 in pack.get_items())

    def test_fail_special_offer(self):
        self.set_requests()
        self.set_placeholders()
        pack = self.offer.apply([self.veg_pizza, self.veg_pizza2])
        self.assertIsNone(pack)

    def test_placeholder(self):
        self.set_requests()
        self.set_placeholders()
        self.assertFalse(self.ph2.is_set())
        self.assertFalse(self.ph1.accept(self.veg_pizza))
        self.assertTrue(self.ph2.accept(self.veg_pizza))
        self.assertTrue(self.ph2.is_set())
        self.assertFalse(self.ph1.is_set())
        self.assertFalse(self.ph2.accept(self.veg_pizza2))

    def test_priced_set(self):
        self.set_requests()
        ps = PricedSet([self.pizza], 750)
        self.assertEqual(self.pizza.get_price(), 1000)
        self.assertEqual(ps.get_price(), 750)
        self.assertEqual(ps.calc_applied_discount(), 250)

    def test_drinks(self):
        juice = Drink("Jugo", LiquidSize(250), 500)
        coke = Drink("Coca Cola", LiquidSize(500), 900)
        self.assertTrue(juice.is_drink())
        self.assertTrue(coke.is_drink())
        self.assertFalse(juice.is_pizza())
        self.assertFalse(juice.is_food())
        self.assertEqual(juice.get_price(), 500)
        self.assertEqual(juice.get_size(), 250)
        self.assertEqual(juice.get_satiety_index(), 250)
        self.assertFalse(juice.has_tag("Lactose"))

    def test_type_constraints(self):
        p = Pizza("A Pizza", DiameterSize(10), 1)
        d = Drink("A Drink", LiquidSize(100), 1)
        is_p = IsPizzaConstraint()
        is_d = IsDrinkConstraint()
        is_f = IsFoodConstraint()
        self.assertTrue(is_p.accept(p))
        self.assertTrue(is_d.accept(d))
        self.assertTrue(is_f.accept(p))
        self.assertFalse(is_p.accept(d))
        self.assertFalse(is_d.accept(p))
        self.assertFalse(is_f.accept(d))

    def test_size_constraints(self):
        p = Pizza("A Pizza", DiameterSize(10), 1)
        d = Drink("A Drink", LiquidSize(100), 1)
        cm10p = SizeConstraint(DiameterSize(10))
        cm20p = SizeConstraint(DiameterSize(20))
        cm100p = SizeConstraint(DiameterSize(100))
        cc100d = SizeConstraint(LiquidSize(100))
        cc10d = SizeConstraint(LiquidSize(10))

        self.assertTrue(cm10p.accept(p))
        self.assertTrue(cc100d.accept(d))
        self.assertFalse(cm20p.accept(p))
        self.assertFalse(cc10d.accept(d))

        self.assertFalse(cc10d.accept(p))
        self.assertFalse(cm100p.accept(d))

if __name__ == '__main__':
    unittest.main()
