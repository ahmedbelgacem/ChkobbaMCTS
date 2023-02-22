from enum import Enum


class Suit(Enum):
    SPADES: int = 1
    HEARTS: int = 2
    DIAMONDS: int = 3
    CLUBS: int = 4


class Card:
    def __init__(self, number, suit: Suit):
        if number not in range(1,11):
            raise ValueError('number should be between 1 and 10')
        self.number = number
        self.suit = suit
    def __str__(self):
        return f'{self.number} of {self.suit.value}'
