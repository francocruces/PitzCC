import abc
from model.Request import Request


class Optimizator(metaclass=abc.ABCMeta):

    """
    An optimizator, calculates the best options
    according to its priorities using the promotions and
    the items price
    """

    """
    :param pricedSets: an array of PricedSet's
    """
    def __init__(self, pricedSets):
        self.pricedSets = pricedSets

    """
    :param requirements: represents what the user wants
    :type requirements: Request
    :return: the priced sets that doesn't violate the request
    """
    def cleanedPricedSets(self, requirements):
        newPricedSets = []

        for set in self.pricedSets:
            aux = True
            for item in set.getItems:
                aux = aux and requirements.eval_item(item)
            if (aux):
                newPricedSets += [set]

        return newPricedSets




    """
    Returns an array of PricedSet's that represents the best options
    :param requirements: represents what the user wants
    :type requirements: Request
    @return an array of PricedSet's that represents the best options
    """
    @abc.abstractmethod
    def getOptions(self, requirements):
        pass

class MoneyOptimizator(Optimizator):

    def __init__(self, pricedSets):
        Optimizator.__init__(self, pricedSets)

    #def getOptions(self, requirements):
