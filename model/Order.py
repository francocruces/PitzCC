from model.Request import Request


class Order:
    def __init__(self):
        self.requests = {}

    # TODO: Catch key errors

    def add_person(self, person_id):
        self.requests[person_id] = Request()

    def add_constraint(self, person_id, constraint):
        self.requests[person_id].add_constraint(constraint)
