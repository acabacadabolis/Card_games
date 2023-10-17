# Card_games

BlackJack on command line game

    Generate random hand for player, random hand for house
    ask to hit or stay, generate cards if hit, pass to house if stay bust if over 21
    house hits if hand value < 17 stay if hard 17 bust if over 21
    compare hands to determine winner.
    

War on the command line game

    Generate random card for User and House
    Compares the card and adds the cards to the winner's deck, in case of a tied, war is declared, adds generate more cards for the war pile and then new cards to compare for User and House. Check winner after user stops playing and gives option of a new game.
    Class Card
        values
            numerical value
            suit
    Class Player
        name
        hand = list of cards
        loop thru the hand to give total hand value