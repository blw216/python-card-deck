class ShuffleError(Exception):
    def __init__(self, n):
        self.n = n
        if self.n <= 1:
            print(f"The deck contains {self.n} card(s) Shuffling not logical and/or possible.")

class DealError(Exception):
    def __init__(self, n):
        self.n = n
        if self.n < 1:
            print(f"The deck has {self.n} cards, therefore there are no cards left to deal.")