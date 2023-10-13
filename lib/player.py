from card import Card

class Player():

    def __init__(self, name) -> None:
        self.name = name
        self.hand = []
    
    def get_hand_value(self):
        total = 0
        for card in self.hand:
            if card.value > 10:
                total += 10
            else:
                total += card.value
        return total
    
    def new_card(self):
        Card(self)