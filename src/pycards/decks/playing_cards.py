import random
from ..base_deck import BaseDeck
from ..exceptions import ShuffleError, DealError

class PlayingCards(BaseDeck):
    """
    PlayingCards is an implementation of the BaseDeck
    abstract class, consisting of the standard deck of
    playing cards.
    """
    def __init__(self):
        """
        This class represents a standard 52-card playing deck. It is
        an extension of the `BaseDeck` abstract base class, which
        requires two methods, "shuffle", and "deal_one_card".
        """
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.deck = [{'rank': rank, 'suit': suit} for rank in self.ranks for suit in self.suits]
        self.deck_length = len(self.deck)

    def shuffle(self):
        """
        The shuffle method performs the Fisher-Yates/Knuth
        shuffling algorithm, which randomly shuffles the
        elements present in a finite list:

        https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle

        This method has no parameters.

        :returns: None
        :raises DeckError: raises a DeckError exception if the deck cannot
        be shuffled.
        """
        # Get the length of the list
        if self.deck_length > 1:
            # Perform the Fisher-Yates/Knuth shuffle
            for i in range(n - 1, 0, -1):
                # Generate a random index between 0 and i (inclusive)
                j = random.randint(0, i)
                # Swap elements at i and j
                self.deck[i], self.deck[j] = self.deck[j], self.deck[i]
        else:
            raise ShuffleError(self.deck_length)
    
    def deal_one_card(self):
        if len(self.deck) > 0:
            print(self.deck_length)
            card = self.deck.pop(0)
            self.deck_length = len(self.deck)
            return card
        else:
            raise DealError(self.deck_length)