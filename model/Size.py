import abc
import math


class Size(metaclass=abc.ABCMeta):
    def __init__(self, number):
        self.nominal_size = number

    def get_nominal_size(self):
        return self.nominal_size

    @abc.abstractmethod
    def get_real_size(self):
        """
        Returns an standard satiety index.
        :return:
        """
        # TODO: Declare satiety index standard
        pass

    def equal(self, size):
        """
        Compares two Size objects
        :param size:
        :type size: Size
        :return: True if are of the same type and have same nominal size
        """
        return type(self) is type(size) and self.nominal_size == size.nominal_size


class DiameterSize(Size):
    def __init__(self, n):
        super(DiameterSize, self).__init__(n)

    def get_real_size(self):
        # Returns volume of a disc with a width of 1 cm
        return math.pi * math.pow(self.nominal_size / 2.0, 2.0)  # In cm^3


class LiquidSize(Size):
    def __init__(self, n):
        super(LiquidSize, self).__init__(n)

    def get_real_size(self):
        return self.nominal_size
