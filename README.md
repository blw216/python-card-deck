# python-card-deck
Deck of cards implemented in Python. 

Instructions:

clone the repo locally: `git clone git@github.com:blw216/python-card-deck.git`

cd to the repo: `cd ./python-card-deck`

pip install the `pycards` package: `pip install .`

run tests: `cd tests && pytest -rxp`

Basic example:

```
from pycards.decks.playing_cards import PlayingCards

# Instantiate the PlayingCards object
card_deck = PlayingCards()

# Shuffle the playing cards
card_deck.shuffle()

# Deal a single card
card = card_deck.deal_one_card()
print(card)

>>> {'rank': '2', 'suit': 'Hearts'}
```
