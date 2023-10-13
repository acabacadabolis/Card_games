from random import randint
class Card():

    def __init__(self, player) -> None:
        self.value = randint(1,13)
        player.hand.append(self)

    def get_card_name(self):
        cards = {
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
        return cards[f"{self.value}"]