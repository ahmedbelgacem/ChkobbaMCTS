from card import Card, Suit
from random import shuffle


# class Deck:
#     def __init__(self, cards):
#         self.cards = cards
#     def __iter__(self):
#         for card in self.cards:
#             yield card
#     def __len__(self):
#         return len(self.cards)
#
#     def __getitem__(self, idx):
#         return self.cards[idx]
#
#
class Deck:
    def __init__(self):
        self.cards = []
        for i in range(1, 11):
            for suit in Suit:
                self.cards.append(Card(i, suit))
        shuffle(self.cards)

    def __str__(self):
        return " ".join([str(card) for card in self.cards])

    def __len__(self):
        return len(self.cards)

    def split(self, position: int):
        if position >= len(self.cards)  or position <= 1:
            raise IndexError('Split index out of range')
        idx = 40 - position
        card = self.cards.pop(idx)
        self.cards = self.cards[idx:] + self.cards[:idx]
        return card

    def draw(self):
        return self.cards.pop()