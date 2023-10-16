from random import randint
class Card():

    def __init__(self, player) -> None:
        self.value = randint(1,13)
        self._suit = randint(1,4)
        player.hand.append(self)

    @property
    def name(self):
        values = {
            "2":"2",
            "3":"3",
            "4":"4",
            "5":"5",
            "6":"6",
            "7":"7",
            "8":"8",
            "9":"9",
            "10":"10",
            "11":"J",
            "12":"Q",
            "13":"K",
            "1":"A"
        }
        return values[f"{self.value}"]

    @property
    def suit(self):
        cards = {
            "1":"♠",
            "2":"♥",
            "3":"♣",
            "4":"♦"
        }
        return cards[f"{self._suit}"]
    
    def __repr__(self) -> str:
        return f"{self.name}{self.suit}"