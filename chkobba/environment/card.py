from enum import Enum


class Suit(str, Enum):
    def __new__(cls, encoding: int, repr: str): # Adds attributes to each object of enum
        obj = str.__new__(cls, '')
        obj._value_ = encoding
        obj.repr = repr
        return obj
    SPADES: tuple = (1, '♠')
    HEARTS: tuple = (2, '♠')
    DIAMONDS: tuple = (3, '♦')
    CLUBS: tuple = (4, '♣')


class Card:
    def __init__(self, number, suit: Suit):
        if number not in range(1,11):
            raise ValueError('Number should be between 1 and 10')
        self.number = number
        self.suit = suit
    def __str__(self):
        return ('┌─────┐\n' + '│{:>5}│\n' + '│{:^5}│\n' + '│{:<5}│\n' + '└─────┘').format(self.suit.repr, self.number, self.suit.repr)
