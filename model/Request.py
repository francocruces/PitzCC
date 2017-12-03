class Request:
    """
    A request emitted by a user. Supports tag constraints.
    """

    def __init__(self):
        self.constraints = []

    # TODO: Implement food amount requests

    def add_constraint(self, cons):
        """
        Add a constraint to this request.
        :param cons: A constraint
        :type cons: Constraint
        :return: self for chaining
        """
        self.constraints.append(cons)
        return self

    def eval_item(self, item):
        for c in self.constraints:
            if not c.accept(item):
                return False
        return True
