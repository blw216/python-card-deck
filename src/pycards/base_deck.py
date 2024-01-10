from typing import List
from abc import ABC, abstractmethod


class BaseDeck(ABC):
    """
    BaseDeck is an abstract base class for defining
    a class template for any subclasses that inherit
    from this class. It is intended to enforce a consitent
    interface for any card deck extensions made to the pycards
    module.
    """

    @abstractmethod
    def shuffle(self):
        """
        This method has no parameters.
        """
        pass

    @abstractmethod
    def deal_one_card(self):
        """
        This method has no parameters.
        """
        pass
