import abc


class Optimizator(metaclass=abc.ABCMeta):
    """
    An optimizator, calculates the best options
    according to its priorities using the promotions and
    the items price
    """

    def __init__(self, pricedSets):
        """
        Creates a new instance of pricedSets
        :param pricedSets: an array of PricedSet's
        """
        self.pricedSets = pricedSets


    def cleanedPricedSets(self, requirements):
        """
        Takes the priced sets and
        :param requirements: represents what the user wants
        :return: the priced sets that doesn't violate the request
        """
        newPricedSets = []

        for set in self.pricedSets:
            aux = True
            for item in set.getItems:
                aux = aux and requirements.eval_item(item)
            if (aux):
                newPricedSets += [set]

        self.pricedSets = newPricedSets

    @abc.abstractmethod
    def getOptions(self, requirements):
        """
        Returns an array of PricedSet's that represents the best options
        :param requirements: represents what the user wants
        :type requirements: Request
        @return an array of PricedSet's that represents the best options
        """
        pass

class PizzaOptimizator(Optimizator):

    def __init__(self, pricedSets):
        Optimizator.__init__(self, pricedSets)

    def getOptions(self, requirements):

