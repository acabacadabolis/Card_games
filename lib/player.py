from card import Card

class Player():

    def __init__(self, name) -> None:
        self.name = name
        self.hand = []
    
    def new_card(self):
        Card(self)