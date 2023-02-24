from environment.deck import Deck
from environment.player import Player


class Game:
    def __init__(self, total_points):
        if total_points not in (11, 21):
            raise ValueError("total points should be either 11 or 21")
        else:
            self.total_points = total_points
        self.player_turn = 0
        self.players = [Player(), Player()]
        self.table = []

    def new_round(self, split_position):
        self.deck = Deck()
        print(self.deck)
        self.__first_card = self.deck.split(split_position)
        return self.__first_card

    def first_play(self, keep: bool):
        if keep:
            self.players[self.player_turn].take([*self.deck.draw(2), self.__first_card])
            self.players[1 - self.player_turn].take(self.deck.draw(3))
            self.table = self.deck.draw(4)
        else:
            self.table = [*self.deck.draw(3), self.__first_card]
            for player in self.players:
                player.take(self.deck.draw(3))
