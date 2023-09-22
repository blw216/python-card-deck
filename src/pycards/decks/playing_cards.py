import random
from ..base_deck import BaseDeck
from ..exceptions import ShuffleError, DealError

class PlayingCards(BaseDeck):
    """
    PlayingCards is an implementation of the BaseDeck abstract class,
    consisting of the standard deck of 52 playing card across four suites.
    """
    def __init__(self):
        """
        This constructor method represents a standard 52-card playing deck.
        """
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.deck = [{'rank': rank, 'suit': suit} for rank in self.ranks for suit in self.suits]
        self.num_cards = len(self.deck)

    def shuffle(self) -> None:
        """
        The shuffle method performs the Fisher-Yates/Knuth
        shuffling algorithm, which randomly shuffles the
        elements present in a finite list:

        https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle

        This method has no parameters.

        :returns: None
        :raises ShuffleError: raises a ShuffleError exception if the deck cannot
        be shuffled.
        """
        # Get the length of the list
        if self.num_cards > 1:
            # Perform the Fisher-Yates/Knuth shuffle
            for i in range(self.num_cards - 1, 0, -1):
                # Generate a random index between 0 and i (inclusive)
                j = random.randint(0, i)
                # Swap elements at i and j
                self.deck[i], self.deck[j] = self.deck[j], self.deck[i]
        else:
            raise ShuffleError(self.num_cards)
    
    def deal_one_card(self) -> dict:
        """
        The `deal_one_card` method returns the "top" (position 0) card
        of the deck at the time the method is called. The dealt card
        is subsequently removed from the deck when it is dealt.

        This method has no parameters.

        :returns: card
        :rtype: [dict | None]
        :raises DealError: This exception is raised if there are no cards
        left to deal.
        """
        # If there are cards left to deal
        if self.num_cards > 0:
            # Extract the top card of the deck
            card = self.deck.pop(0)
            # Recalculate the number of cards left in the deck
            self.num_cards = len(self.deck)
            # Return the card to the user
            return card
        # Else raise the DealError exception
        else:
            raise DealError(self.num_cards)