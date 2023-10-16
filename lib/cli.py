from card import Card
from player import Player


## Placeholder variables
card = []
hand_total = 0
house_card = 0
house_total = 0
chatter = ""
yes = "hit" or "HIT" or "y" or "Y" or "YES" or "yes"
no = "stay" or "STAY" or "n" or "N" or "NO" or "no"
answer = None
# player_wins = 0 ## Log how many wins the player has
# player_money = 0 ## player should be able to bet? Idk

def splash_screen(): ## Figure out what to display when the user boots the program
    pass

def banter(): ## Display banter/chatter from the House Dealer
    pass

def input_text(): ## This will allow the user to input text at certain moments
    pass

def player_hit_stay(): ## What is displayed when you want to hit or stay
    input_text()
    if answer == yes: ## If they want to hit generate new card
        user.new_card()
    elif answer == no:
        pass
    
def display_hand(player):
    player.hand


def lose(): ## What is displayed when you BUST
    pass

def win(): ## What is displayed when you WIN
    pass


def game_logic():


## TODO Input of Hit/Stay Play Again 

    ## Instant WIN/LOSE conditions
    if user.get_hand_value > 21 or house.get_hand_value == 21:
        lose()
    if user.get_hand_value == 21 or house.get_hand_value < 21:
        win()
    ## Secondary Win/Lose conditions --- on STAY
    if house.stay == True:
        if user.get_hand_value <= house.get_hand_value: ## and house_get_hand_value < 21 REDUNDANT
            lose()
        elif user.get_hand_value > house.get_hand_value: ## and house_get_hand_value < 21 REDUNDANT
            win()
        ## Splitting on doubles



## Just adding to make something new for Github