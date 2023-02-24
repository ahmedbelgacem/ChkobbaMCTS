from environment.card import Card, Suit
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
        output = ''
        chunk_size = 10
        chunks = [self.cards[i:i + chunk_size] for i in range(0, len(self.cards), chunk_size)]
        for chunk in chunks:
            output += '┌─────┐ ' * len(chunk) + '\n' + \
                      ('│{:>5}│ ' * len(chunk)).format(*[card.suit.repr for card in chunk]) + '\n' + \
                      ('│{:^5}│ ' * len(chunk)).format(*[card.number for card in chunk]) + '\n' + \
                      ('│{:<5}│ ' * len(chunk)).format(*[card.suit.repr for card in chunk]) + '\n' + \
                      '└─────┘ ' * len(chunk) + '\n'
        return output

    def __len__(self):
        return len(self.cards)

    def split(self, position: int):
        if position >= len(self.cards) or position <= 1:
            raise IndexError('Split index out of range')
        idx = len(self.cards) - position
        card = self.cards.pop(idx)
        self.cards = self.cards[idx:] + self.cards[:idx]
        return card

    def draw(self, cards_number):
        drawn_cards = []
        for _ in range(cards_number):
            drawn_cards.append(self.cards.pop())
        return drawn_cards
