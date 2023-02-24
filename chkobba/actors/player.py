from environment import Board, Card

class Player:
  def __init__(self) -> None:
    self.hand = []
    self.pocket = [] # Face down cards (cards player has acquired)
    self.score = 0
    
  @property
  def _score(self):
    pass
  
  def place(self, card: Card):
    try:
      self.hand.remove(card)
    except:
      raise ValueError('Player does not have card in hand')