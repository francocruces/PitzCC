from model.Constraint import RejectTagConstraint, RequireTagConstraint
from model.Order import Order


# TODO: Implement


class ScraperWrapper:
    def __init__(self):
        self.database = []

    def store_data(self):
        # Do something with scraped data
        pass


class OptimizerWrapper:
    def __init__(self, order):
        self.order = order
        self.database = []

    def load_database(self):
        # Get data from somewhere into self.database
        pass


class BotWrapper:
    def __init__(self):
        self.order = Order()
        self.database = []

    def reject_tag(self, person_id, tag):
        self.order.add_constraint(person_id, RejectTagConstraint(tag))

    def require_tag(self, person_id, tag):
        self.order.add_constraint(person_id, RequireTagConstraint(tag))

    def set_amount_of_food(self, amount):
        # TODO: Discuss and design
        pass

    def set_amount_of_liquid(self, amount):
        # TODO: Discuss and design
        pass
