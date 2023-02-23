from environment import Card

class Board:
  def __init__(self) -> None:
    self.cards = []
    
  def __str__(self):
    output = ''
    chunk_size = 4
    chunks = [self.cards[i:i + chunk_size] for i in range(0, len(self.cards), chunk_size)]
    for chunk in chunks:
        output += '┌─────┐ '*len(chunk) + '\n' + \
                ('│{:>5}│ '*len(chunk)).format(*[card.suit.repr for card in chunk]) + '\n' + \
                ('│{:^5}│ '*len(chunk)).format(*[card.number for card in chunk]) + '\n' + \
                ('│{:<5}│ '*len(chunk)).format(*[card.suit.repr for card in chunk])+ '\n' + \
                '└─────┘ '*len(chunk) + '\n'
    return output
      
  def place(self, card: Card):
    self.cards.append(card)
  
  def take(self, card: Card):
    try:
      self.cards.remove(card)
    except:
      raise ValueError('Card is not in board')