import abc


class Constraint(metaclass=abc.ABCMeta):
    """
    An abstract Constraint. Implements common functionality for constraints
    """
    @abc.abstractmethod
    def accept(self, item):
        """
        Accepts or rejects given item according to the Constraint rules.
        :param item: A menu element to evaluate
        :type item: MenuElement
        :return: True if accepts, False otherwise
        """
        pass


class RequireTagConstraint(Constraint):
    """
    Constraint that requires a tag to be present.
    """

    def __init__(self, tag):
        super(RequireTagConstraint, self).__init__()
        self.tag = tag

    def accept(self, item):
        return item.has_tag(self.tag)


class RejectTagConstraint(Constraint):
    """
    Constraint that requires a tag not to be present.
    """

    def __init__(self, tag):
        super(RejectTagConstraint, self).__init__()
        self.tag = tag

    def accept(self, item):
        return not item.has_tag(self.tag)
