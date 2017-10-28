import abc
from abc import ABCMeta

from model.Menu import MenuElement


class Request:
    """
    A request emitted by a user. Supports tag constraints.
    """

    def __init__(self):
        self.constraints = []

    # TODO: Implement generic requests

    def add_constraint(self, cons):
        """
        Add a constraint to this request.
        :param cons: A constraint
        :type cons: Constraint
        :return: self for chaining
        """
        self.constraints.append(cons)
        return self


class Constraint:
    """
    An abstract Constraint. Implements common functionality for constraints
    """
    __metaclass__ = ABCMeta

    @abc.abstractmethod
    def eval(self, item):
        """
        Accepts or rejects given item according to the Constraint rules.
        :param item: A menu element to evaluate
        :type item: MenuElement
        :return: True if accepts, False otherwise
        """
        return True


class RequireTagConstraint(Constraint):
    """
    Constraint that requires a tag to be present.
    """
    def __init__(self, tag):
        super(RequireTagConstraint, self).__init__()
        self.tag = tag

    def eval(self, item):
        return item.has_tag(item)


class RejectTagConstraint(Constraint):
    """
    Constraint that requires a tag not to be present.
    """
    def __init__(self, tag):
        super(RejectTagConstraint, self).__init__()
        self.tag = tag

    def eval(self, item):
        return not item.has_tag(item)
