import abc

from model.Menu import MenuElement, SizedElement
from model.Size import Size


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


class TypeConstraint(Constraint):
    def __init__(self):
        super(TypeConstraint, self).__init__()

    @abc.abstractmethod
    def accept(self, item):
        pass


class IsPizzaConstraint(TypeConstraint):
    def __init__(self):
        super(IsPizzaConstraint, self).__init__()

    def accept(self, item):
        """
        :type item: MenuElement
        :rtype bool
        """
        return item.is_pizza()


class IsFoodConstraint(TypeConstraint):
    def __init__(self):
        super(IsFoodConstraint, self).__init__()

    def accept(self, item):
        """
        :type item: MenuElement
        :rtype bool
        """
        return item.is_food()


class IsDrinkConstraint(TypeConstraint):
    def __init__(self):
        super(IsDrinkConstraint, self).__init__()

    def accept(self, item):
        """
        :type item: MenuElement
        :rtype bool
        """
        return item.is_drink()


class SizeConstraint(Constraint):
    def __init__(self, size):
        """
        Constructor.
        :param size:
        :type size: Size
        """
        super(SizeConstraint, self).__init__()
        self.size = size

    def accept(self, item):
        """
        :type item: SizedElement
        :rtype bool
        """
        return self.size.equal(item.get_size_object())
