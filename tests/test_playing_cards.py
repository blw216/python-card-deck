from pycards.decks.playing_cards import PlayingCards
from pycards.exceptions import ShuffleError, DealError
import pytest

class TestPlayingCards:
    def test_basic_shuffling(self):
        card_deck = PlayingCards()
        deck_start = card_deck.deck.copy()
        assert card_deck.deck == deck_start
        card_deck.shuffle()
        assert card_deck.deck != deck_start

    def test_shuffle_error(self):
        # Exception should be raised if number of cards < 1
        card_deck = PlayingCards()
        card_deck.shuffle()
        # Deal all but one card
        [card_deck.deal_one_card() for i in range(0, 51, 1)]
        with pytest.raises(ShuffleError):
            card_deck.shuffle()
    
    def test_deal_card_basic(self):
        card_deck = PlayingCards()
        num_start_cards = card_deck.num_cards
        card_deck.shuffle()
        card_deck.deal_one_card()
        assert card_deck.num_cards == num_start_cards - 1

    def test_deal_card_empty_deck(self):
        card_deck = PlayingCards()
        card_deck.shuffle()
        [card_deck.deal_one_card() for i in range(0, 52, 1)]
        with pytest.raises(DealError):
            card_deck.deal_one_card()



