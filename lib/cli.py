from card import Card
from player import Player
from random import randint
import os
import ipdb


## Placeholder variables
card = []
hand_total = 0
house_card = 0
house_total = 0
chatter = ""
yes = ["hit", "HIT", "y", "Y", "YES","yes"]
no = "stay" or "STAY" or "n" or "N" or "NO" or "no"
# player_wins = 0 ## Log how many wins the player has
# player_money = 0 ## player should be able to bet? Idk

def init_match_board(player):
    for x in range(5): ## Only Generate 5 of the 9 cards 4 will be duplicates
        player.new_card()
    match_hand = []
    for i in range(4): ## Duplicates of the 4 cards
        match_hand.append(player.hand[i]) 
    board = { ## Dictionary of Board to call for A1, A2, etc.
    "A1": player.hand.pop(randint(0,4)),
    "A2": match_hand.pop(randint(0,3)),
    "A3": player.hand.pop(randint(0,3)),
    "B1": match_hand.pop(randint(0,2)),
    "B2": player.hand.pop(randint(0,2)),
    "B3": match_hand.pop(randint(0,1)),
    "C1": player.hand.pop(randint(0,1)),
    "C2": match_hand.pop(),
    "C3": player.hand.pop()
     }

    return board

def display_hand(player):
    print(f"{player.name} hand: {player.hand}")
    print(f'{player.name} total: {player_hand_value(player)}')

def war_hand(player):
    if len(player.hand):
        player.hand[0] = Card(player)
        player.hand[1] = Card(player)
    else:
        player.new_card()
        player.new_card()
    print(f"User's Card:{player.hand[0]}\nHouse's Card:{player.hand[1]}")

def war_clear_board(player):
    for i in range(len(player.hand)):
        player.hand.pop(0)

def win(player, player2): ## Check if a player won
    if 21 > player_hand_value(player) > player_hand_value(player2) :
        return True
    return False

## INSTANT WIN / LOSE

def instant_lose(player): ## Check if this player instantly lost
    if player_hand_value(player) > 21:
        return True
    return False

def instant_win(player): ## Check if this player instantly won
    if player_hand_value(player) == 21:
        return True
    return False

def player_hand_value(player):
    total = 0
    for card in player.hand:
        if "A" in card.name:
            total += 11
        elif "J" in card.name or "Q" in card.name or "K" in card.name:
            total += 10
        else:
            total += card.value
    for card in player.hand:
        if "A" == card.name:
            if total > 21:
                total - 10
    return total

def blackjack():
    os.system('clear') ## Clear Screen
    ## Define the players names
    user = Player("user")
    house = Player("house")
    answer = None
    ##Game Start
    user.new_card()
    user.new_card()
    house.new_card()
    house.new_card()
    display_hand(user)
    display_hand(house)
    ##User Turn
    if not instant_win(house):
        answer = input("Would you like to HIT or STAY? \n")
    while answer in yes:
        print('Here ya go fella')
        user.new_card()
        display_hand(user)
        if instant_lose(user):
            print(f'{user.name} has bust')
            break
        elif instant_win(user):
            print(f'Looks like ya won ya sumvabitch!')
            break
        else:
            answer = input("Would you like to HIT or STAY? \n")
    ##House Turn
    if not (instant_win(user) or instant_lose(user)):
        print("\n")
        while player_hand_value(house)<17:
            house.new_card()
            display_hand(house)
        if instant_lose(house):
            print(f'{house.name} has bust')
        elif instant_win(house):
            print(f'House always wins')
        elif win(user, house):
            print(f'Looks like ya won ya sumvabitch!')
        elif win(house, user):
            print(f'House always wins')
        else:
            print("Evenly matched")
    ##Replay Option
    repeat = input("would you like to play again? \n")
    if repeat in yes:
        blackjack()

def war():
    os.system('clear') ## Clear Screen
    user = Player("user")
    house = Player("house")
    board = Player("board")
    war_pile = Player("pile")
    ##War Round
    repeat = "yes"
    while repeat in yes: ##While user wants to continue current game
        war_hand(board)

        while len(board.hand):  ##While there are cards on the board
            if board.hand[0].value > board.hand[1].value:   ##User wins round
                user.hand.append(board.hand.pop())
                user.hand.append(board.hand.pop())
                if len(war_pile.hand):
                    for i in range(len(war_pile.hand)):
                        user.hand.append(war_pile.hand[i])
                    war_clear_board(war_pile)
                print(f"User's Deck {user.hand}")
                print(f"House's Deck {house.hand}")
            elif board.hand[1].value > board.hand[0].value:    ##House wins round
                house.hand.append(board.hand.pop())
                house.hand.append(board.hand.pop())
                if len(war_pile.hand):
                    for i in range(len(war_pile.hand)):
                        house.hand.append(war_pile.hand[i])
                    war_clear_board(war_pile)
                print(f"User's Deck {user.hand}")
                print(f"House's Deck {house.hand}")
            elif board.hand[1].value == board.hand[0].value:    ##Round is tied
                war_pile.hand.append(board.hand.pop())
                war_pile.hand.append(board.hand.pop())
                for _ in range(6):
                    war_pile.new_card()
                print(f"War was Declared. War spoils:{war_pile.hand}")
                war_hand(board)
        repeat = input("Continue?\n")
    if len(user.hand) > len(house.hand):
        print("You've Won")
    elif len(user.hand) < len(house.hand):
        print("You've Lost")
    else:
        print("Y'all Tied")
    new_game = input("New Game?\n")
    if new_game in yes:
        war()
##Launch Game
#blackjack()
def match():
    os.system('clear') ## Clear Screen
    player = Player('player')
    board = init_match_board(player)
    print(f'{board["A1"]}  {board["A2"]}  {board["A3"]} ')
    print(f'{board["B1"]}  {board["B2"]}  {board["B3"]} ')
    print(f'{board["C1"]}  {board["C2"]}  {board["C3"]} ')

match()
# game = input("Would you like to player Blackjack or War?\n")
# if game == "War":
#     war()
# if game == "Blackjack":
#     blackjack()
# if game == "Match":
#     match()

