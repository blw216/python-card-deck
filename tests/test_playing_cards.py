from pycards.decks.playing_cards import PlayingCards

class TestPlayingCards:
    def test_shuffling(self):
        card_deck = PlayingCards()
        deck_start = card_deck.deck.copy()
        assert card_deck.deck == deck_start
        card_deck.shuffle()
        assert card_deck.deck != deck_start
