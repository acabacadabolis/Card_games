from card import Card
from player import Player
from random import randint
import ipdb

## Placeholder variables
yes = [ "hit", "y" , "yes" ]

def print_board(board):
    print(f'\033[4m{board["A1"]} | {board["A2"]} | {board["A3"]}\n{board["B1"]} | {board["B2"]} | {board["B3"]}\033[0m\n{board["C1"]} | {board["C2"]} | {board["C3"]}')

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
    print(f"{player.name} hand: \033[1m{player.hand}\033[0m")
    print(f'{player.name} total: \033[1m{player_hand_value(player)}\033[0m')

def war_hand(player):
    if len(player.hand):
        player.hand[0] = Card(player)
        player.hand[1] = Card(player)
    else:
        player.new_card()
        player.new_card()
    print(f"User's Card:\033[1m{player.hand[0]}\033[0m\nHouse's Card:\033[1m{player.hand[1]}\033[0m")

def war_clear_board(player):
    for i in range(len(player.hand)):
        player.hand.pop(0)

def win(player, player2): ## Check if a player won
    if 21 > player_hand_value(player) > player_hand_value(player2) :
        return True
    return False

## INSTANT WIN / LOSE

def instant_win(player): ## Check if this player instantly won
    if player_hand_value(player) == 21:
        return True
    return False

def instant_lose(player): ## Check if this player instantly lost
    if player_hand_value(player) > 21:
        return True
    return False

def player_hand_value(player):
    total = 0
    for card in player.hand:
        if "A" in card.name:##Ace adds 11 to hand value
            total += 11
        elif "J" in card.name or "Q" in card.name or "K" in card.name:
            total += 10
        else:
            total += card.value
    for card in player.hand:
        if "A" == card.name:##Check if Ace is in hand when its over 21 and reduces hand value if it is
            if total > 21:
                total -= 10
    return total

def blackjack():
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
    if instant_win(user):
        print(f'\033[92mLooks like ya won ya sumvabitch!\033[0m')
    if not instant_win(house) and not instant_win(user):
        answer = input("\033[93mWould you like to HIT or STAY?\033[0m\n")
        while answer.lower() in yes:
            print('\033[95mHere ya go fella\033[0m')
            user.new_card()
            display_hand(user)
            if instant_lose(user):
                print(f'\033[91m{user.name} has bust\033[0m')
                break
            elif instant_win(user):
                print(f'\033[92mLooks like ya won ya sumvabitch!\033[0m')
                break
            else:
                answer = input("\033[0mWould you like to HIT or STAY?\033[0m\n")
    ##House Turn
    if not (instant_win(user) or instant_lose(user)):

        while player_hand_value(house) < 17 :
            house.new_card()
            display_hand(house)
        if instant_lose(house):
            print(f'\033[92m{house.name} has bust\033[0m')
        elif instant_win(house):
            print(f'\033[91mHouse always wins\033[0m')
        elif win(user, house):
            print(f'\033[92mLooks like ya won ya sumvabitch!\033[0m')
        elif win(house, user):
            print(f'\033[91mHouse always wins\033[0m')
        else:
            print(f"\033[94mEvenly matched\033[0m")
    ##Replay Option
    repeat = input("\033[93mWould you like to play again?\033[0m\n")
    if repeat.lower() in yes:
        blackjack()
    else:
        game_select = input("\033[93mDifferent Game?\033[0m\n")
    if game_select.lower() in yes:
        program_start()

def war():
    user = Player("user")
    house = Player("house")
    board = Player("board")
    war_pile = Player("pile")
    ##War Round
    repeat = "yes"
    while repeat.lower() in yes: ##While user wants to continue current game
        war_hand(board)

        while len(board.hand):  ##While there are cards on the board
            if board.hand[0].value > board.hand[1].value:   ##User wins round
                user.hand.append(board.hand.pop())
                user.hand.append(board.hand.pop())
                if len(war_pile.hand):
                    for i in range(len(war_pile.hand)):
                        user.hand.append(war_pile.hand[i])
                    war_clear_board(war_pile)
                print(f"User's Deck \033[1m{user.hand}\033[0m")
                print(f"House's Deck \033[1m{house.hand}\033[0m")
            elif board.hand[1].value > board.hand[0].value:    ##House wins round
                house.hand.append(board.hand.pop())
                house.hand.append(board.hand.pop())
                if len(war_pile.hand):
                    for i in range(len(war_pile.hand)):
                        house.hand.append(war_pile.hand[i])
                    war_clear_board(war_pile)
                print(f"User's Deck \033[1m{user.hand}\033[0m")
                print(f"House's Deck \033[1m{house.hand}\033[0m")
            elif board.hand[1].value == board.hand[0].value:    ##Round is tied
                war_pile.hand.append(board.hand.pop())
                war_pile.hand.append(board.hand.pop())
                for _ in range(6):
                    war_pile.new_card()
                print(f"\033[1m\033[95mWar was Declared. War spoils:{war_pile.hand}\033[0m")
                war_hand(board)
        repeat = input("\033[93mContinue?\033[0m\n")
    if len(user.hand) > len(house.hand):
        print("\033[92mYou've Won\033[0m")
    elif len(user.hand) < len(house.hand):
        print("\033[91mYou've Lost\033[0m")
    else:
        print("\033[94mY'all Tied\033[0m")
    new_game = input("\033[93mNew Game?\033[0m\n")
    if new_game.lower() in yes:
        war()
    else:
        game_select = input("\033[93mDifferent Game?\033[0m\n")
    if game_select.lower() in yes:
        program_start()

def match():
    player = Player('player')
    board = init_match_board(player)
    
    hidden_board ={
        "A1": "A1",
        "A2": "A2",
        "A3": "A3",
        "B1": "B1",
        "B2": "B2",
        "B3": "B3",
        "C1": "C1",
        "C2": "C2",
        "C3": "C3"
    }

    guess_board = {
        "A1": "A1",
        "A2": "A2",
        "A3": "A3",
        "B1": "B1",
        "B2": "B2",
        "B3": "B3",
        "C1": "C1",
        "C2": "C2",
        "C3": "C3"
    }
    print_board(guess_board)
    guessing = "yes"
    count_match = 0
    while guessing.lower() in yes:
        guess1 = input("Pick a Card\n")
        if guess1.upper() in board:
            guess_board[f"{guess1.upper()}"] = board[f"{guess1.upper()}"]
            print_board(guess_board)
            guess2 = input("Pick a second Card\n")
            if guess2.upper() in board:
                if guess_board[f"{guess2.upper()}"] != board[f"{guess2.upper()}"]:
                    guess_board[f"{guess2.upper()}"] = board[f"{guess2.upper()}"]
                    print_board(guess_board)
                    if guess_board[f"{guess1.upper()}"] == guess_board[f"{guess2.upper()}"]:
                        print("\033[93mRight guess\033[0m")
                        count_match += 1
                    else:
                        print("\033[91mThey don't match\033[0m")
                        guess_board[f"{guess1.upper()}"] = hidden_board[f"{guess1.upper()}"]
                        guess_board[f"{guess2.upper()}"] = hidden_board[f"{guess2.upper()}"]
                else:
                    print('\033[91mNot a valid guess\033[0m')
            else:
                print('\033[91mNot a valid guess\033[0m')
        else:
            print('\033[91mNot a valid guess\033[0m')
        if count_match < 3:
            pass
        elif count_match == 4:
            print("\033[92mYou won\033[0m")
            guessing = "asd"
    repeat = input("Play again?\n")
    if repeat in yes:
        match()
    new_game = input("Play a different game?\n")
    if new_game in yes:
        program_start()

def program_start():
    game = input("\033[93mWould you like to player Blackjack or War?\033[0m\n")
    if game.lower() == "war":
        war()
    if game.lower() == "blackjack":
        blackjack()
    if game.lower() == "matching":
        match()
        
program_start()