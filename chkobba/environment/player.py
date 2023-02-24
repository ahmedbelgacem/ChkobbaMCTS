class Player:
    def __init__(self) -> None:
        self.hand = []

    def take(self, cards):
        self.hand = cards
