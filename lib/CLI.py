## Placeholder variables
card = []
hand_total = 0
house_card = 0
house_total = 0
chatter = ""
yes = "hit" or "HIT" or "y" or "Y" or "YES" or "yes"
no = "stay" or "STAY" or "n" or "N" or "NO" or "no"
answer = None

def splash_screen(): ## Figure out what to display when the user boots the program
    pass

def banter(): ## Display banter/chatter from the House Dealer
    pass

def input_text(): ## This will allow the user to input text at certain moments
    pass

def player_hit_stay(): ## What is displayed when you want to hit or stay
    input_text()
    if answer == yes: ## If they want to hit generate new card
        player.new_card()
    elif answer == no:
        pass
    


def lose(): ## What is displayed when you BUST
    

def win(): ## What is displayed when you WIN
    pass


def game_logic():
    ## Instant WIN/LOSE conditions
    if user.get_hand_value > 21 or house.get_hand_value == 21:
        lose()
    if user.get_hand_value == 21 or house.get_hand_value < 21:
        win()
    ## Secondary Win/Lose conditions --- on STAY
    if house.stay == True:
        if user.get_hand_value < house.get_hand_value and house_get_hand_value < 21:
            lose()
        elif user.get_hand_value >= house.get_hand_value and house_get_hand_value < 21:
            win()
