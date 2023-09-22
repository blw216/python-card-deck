from pycards.decks.playing_cards import PlayingCards
from pycards.exceptions import ShuffleError, DealError
import pytest

class TestPlayingCards:
    def test_basic_shuffling(self):
        """
        Basic test to ensure shuffling functionality. Odds of
        a 52 card random shuffle equalling the input deck order
        are astronomically small.
        """
        card_deck = PlayingCards()
        deck_start = card_deck.deck.copy()
        assert card_deck.deck == deck_start
        card_deck.shuffle()
        assert card_deck.deck != deck_start

    def test_shuffle_error(self):
        """
        Test to make sure the deck cannot be shuffled with only
        a single card.
        """
        # Exception should be raised if number of cards < 1
        card_deck = PlayingCards()
        card_deck.shuffle()
        # Deal all but one card
        [card_deck.deal_one_card() for i in range(0, 51, 1)]
        with pytest.raises(ShuffleError):
            card_deck.shuffle()
    
    def test_deal_card_basic(self):
        """
        Test to ensure cards are removed from the deck when dealt.
        """
        card_deck = PlayingCards()
        num_start_cards = card_deck.num_cards
        card_deck.shuffle()
        card_deck.deal_one_card()
        assert card_deck.num_cards == num_start_cards - 1

    def test_deal_card_empty_deck(self):
        """
        Test to ensure that a DealError is raised when a card
        is attempted to be dealt from an empty deck.
        """
        card_deck = PlayingCards()
        card_deck.shuffle()
        [card_deck.deal_one_card() for i in range(0, 52, 1)]
        with pytest.raises(DealError):
            card_deck.deal_one_card()



