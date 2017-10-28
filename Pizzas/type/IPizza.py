from abc import ABCMeta, abstractmethod

'''
IPizza
An interface with methods that all pizzas should have
'''


class IPizza(metaclass=ABCMeta):

    '''
    Returns the pizza's price
    @return the pizza's price : int
    '''
    @abstractmethod
    def getPrice(self):
        pass

    '''
    Returns the ingredients
    @return an array with the ingredients : Ingredient[]
    '''
    @abstractmethod
    def getIngredients(self):
        pass

    '''
    Returns the pizza size
    @return a string that represents the pizza size : str
    '''
    @abstractmethod
    def getSize(self):
        pass

    '''
    Returns the name of the pizza
    @return a string with the name of the pizza : str
    '''
    @abstractmethod
    def getName(self):
        pass

    '''
    Returns true if the pizza has an ingredient
    @param ingredient: is the indredient that is going to be checked
    @return True if the ingredient is in the pizza, False if it isn't
    '''
    @abstractmethod
    def hasIngredient(self, anIngredient):
        pass

