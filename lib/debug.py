import ipdb;
from card import Card
from player import Player


if __name__ == "__main__":

    player = Player('some_guy')
    card1 = Card(player)
    card2 = Card(player)

    ipdb.set_trace()