from card import Card
from player import Player
import ipdb


## Placeholder variables
card = []
hand_total = 0
house_card = 0
house_total = 0
chatter = ""
yes = ["hit", "HIT", "y", "Y", "YES","yes"]
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

def display_hand(player):
    print(f"Your hand: {player.hand}")
    total = player_hand_value(player)
    print(f'Your total: {total}')


def lose(player): ## What is displayed when you BUST
    if player_hand_value(player) > 21:
        return True
    return False

def win(player, player2): ## What is displayed when you WIN
    if player_hand_value(player) == 21 or 21 > player_hand_value(player) > player_hand_value(player2) :
        return True
    return False

def player_hand_value(player):
    total = 0
    for card in player.hand:
        if "A" in card.name:
            if (total + 11) <= 21:
                total += 11
            else:
                total += 1
        elif "J" in card.name or "Q" in card.name or "K" in card.name:
            total += 10
        else:
            total += card.value
    return total


def game_logic():
    ## Define the players names
    user = Player("user")
    house = Player("house")

## GAME START
    user.new_card()
    user.new_card()
    house.new_card()
    house.new_card()
    # ipdb.set_trace()
    display_hand(user)
    # print("Would you like to HIT or STAY?")
    ## Get user input
    answer = input("Would you like to HIT or STAY? \n")
    while answer in yes and not lose(user):
        print('Here ya go fella')
        user.new_card()
        display_hand(user)
        lose(user)
        if not lose(user):
            answer = input("Would you like to HIT or STAY? \n")
        if lose(user):
            print(f'{user.name} has bust')
        if win(user, house):
            print(f'Looks like ya won ya sumvabitch!')
        
        
    
    ## if hand is under 21


    # ## Instant WIN/LOSE conditions
    # if user.get_hand_value > 21 or house.get_hand_value == 21:
    #     lose()
    # if user.get_hand_value == 21 or house.get_hand_value < 21:
    #     win()
    # ## Secondary Win/Lose conditions --- on STAY
    # if house.stay == True:
    #     if user.get_hand_value <= house.get_hand_value: ## and house_get_hand_value < 21 REDUNDANT
    #         lose()
    #     elif user.get_hand_value > house.get_hand_value: ## and house_get_hand_value < 21 REDUNDANT
    #         win()
    #     ## Splitting on doubles



## Just adding to make something new for Github
game_logic()