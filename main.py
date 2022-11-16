### Poker Helper Begin Game ###
# This program is designed to help you play poker.
# It will tell you what cards you have and what cards you need to win.

# Ideas: Count number of rounds played, and at the end of the session save the number of rounds played, profit (+/-) to a text file.

from cards import Card
from strategy import *
import sys
import os
import time


# Colors (final)
GREEN = '\033[92m'  # green
YELLOW = "\u001b[38;5;226m"  # yellow
RED = '\033[91m'  # red
# dark grey; to make lighter, increase 238 to anything 255 or below
GREY = '\u001b[48;5;238m'
NO_COLOR = '\033[0m'  # white
BLUE = '\033[34m'  # blue

# Global variables to store player and dealer cards
player_cards = []
dealer_cards = []
best_hand = []

WELCOME = """
  _____      _                _____       _                
 |  __ \    | |              / ____|     | |               
 | |__) |__ | | _____ _ __  | (___   ___ | |_   _____ _ __ 
 |  ___/ _ \| |/ / _ \ '__|  \___ \ / _ \| \ \ / / _ \ '__|
 | |  | (_) |   <  __/ |     ____) | (_) | |\ V /  __/ |   
 |_|   \___/|_|\_\___|_|    |_____/ \___/|_| \_/ \___|_|   
                                                           
                                                           
"""


# Function that clears the user terminal and has support for multiple operating systems
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Main gameplay loop
def game():
    numTurn = 1
    playing = True
    while (numTurn < 5) and playing == True:
        # preflop turn is the first turn
        if numTurn == 1:
            pre_flop()
            playing = call_or_fold()
        # flop occurs on the second turn
        elif numTurn == 2:
            while len(dealer_cards) < 3:
                dealer_cards.append(dealing_cards())
            cls()
            print("These are the cards on the table:")
            print("")
            print_cards(dealer_cards)
            print("These are your cards:")
            print("")
            print_cards(player_cards)
            best_hand = list(current_hand(player_cards, dealer_cards))
            print("Post-flop turn. What would you like to do?")
            playing = call_or_fold()
        # During the 3rd and 4th turns, the dealer simply deals 1 card to the table
        else:
            dealer_cards.append(dealing_cards())
            cls()
            print("These are the cards on the table:")
            print("")
            print_cards(dealer_cards)
            print("These are your cards:")
            print("")
            print_cards(player_cards)
            best_hand = list(current_hand(player_cards, dealer_cards))
            if numTurn == 4:
                break
            else:
                print("Turn #", numTurn, "What would you like to do?")
                playing = call_or_fold()
        numTurn += 1
    # Round is over, because the player has either folded, or the round has concluded
    time.sleep(1)
    print("This round has concluded, enter any key to return to the main menu.")
    returnMenu = input(" >")
    player_cards.clear()
    dealer_cards.clear()
    best_hand.clear()
    time.sleep(1)
    cls()


# First turn during a poker round
def pre_flop():
    firstCard = dealing_cards()
    secondCard = dealing_cards()
    player_cards.append(firstCard)
    player_cards.append(secondCard)
    player_hand1 = ""
    player_hand2 = ""
    suited = "o"
    cls()
    print("")
    player_hand1 += firstCard.value
    player_hand1 += secondCard.value
    player_hand1 += suited
    player_hand2 += secondCard.value
    player_hand2 += firstCard.value
    player_hand2 += suited
    print_cards([firstCard, secondCard])
    # Inform the player the strength of their starting hand
    if (player_hand1 in STier) or (player_hand2 in STier):
        print("Your hand is amazing! [S Tier]")
        print("Suggested play: aggressive preflop raise")
    elif (player_hand1 in ATier) or (player_hand2 in ATier):
        print("Your hand is great. [A Tier]")
    elif (player_hand1 in BTier) or (player_hand2 in BTier):
        print("Your hand is decent. [B Tier]")
    elif (player_hand1 in CTier) or (player_hand2 in CTier):
        print("Your hand is poor. [C Tier]")
        print(
            "Suggested play: fold, unless you're going last. Examine how the other players are betting pre-flop.")
    elif (player_hand1 in DTier) or (player_hand2 in DTier):
        print("Your hand is awful. [D Tier]")
        print(
            "Suggested play: Fold preflop. Only play this hand as a small blind.")
    else:
        print("Your hand is trash!")
        print("Suggested play: fold immediately.")
    if firstCard.suit == secondCard.suit:
        suited = "s"
        print("NOTE: Your cards are suited! Watch for a possible flush draw.")
    print("##################################")
    print("Pre-flop turn. What would you like to do?")


# Dealing a card (to player or the table)
# If argument is true, card is added to player_cards, if false, added to dealer_cards
def dealing_cards():
    ask = ""
    print("A card has been dealt! Please enter the card's value and suit in the following format:")
    print("Ten of Clubs == [Tc]")
    print("Possible card values: 2 3 4 5 6 7 8 9 T J Q K A")
    print("Possible suits: Spades (s), Hearts (h), Clubs (c), Diamonds (d)")
    while True:
        ask = input(" >")
        if ask not in all_possible_cards:
            print("That is not a valid card! Please try again")
        else:
            break
    dealt_card = Card(ask[0], ask[1])  # create the card based on user input
    return dealt_card


# Function that takes user input for each turn during a round.
# Input cleansing so the user cannot cause an input error
def call_or_fold():
    choice = ""
    while choice not in ["1", "2"]:
        print("1. Call/Raise")
        print("2. Fold")
        choice = input(" >")
        if choice == "1":
            print("You have decided to keep playing.")
            return True
        elif choice == "2":
            print("You have decided to fold your hand.")
            return False
        else:
            print("Invalid input! Please try again.")


# Printing ASCII version of playing cards
def print_cards(cards):
    cards_copy = cards.copy()
    empty = Card('?', '?')
    if (len(cards) == 3):
        cards_copy.append(empty)
        cards_copy.append(empty)
    if (len(cards) == 4):
        cards_copy.append(empty)
    suits_name = ['s', 'd', 'h', 'c', '?']
    suits_symbols = [f'{BLUE}♠{NO_COLOR}', f'{RED}♦{NO_COLOR}',
                     f'{RED}♥{NO_COLOR}', f'{BLUE}♣{NO_COLOR}', f'{GREEN}?{NO_COLOR}']
    lines = [[] for i in range(9)]
    for index, card in enumerate(cards_copy):
        # "King" should be "K" and "10" should still be "10"
        if card.value == 'T':  # ten is the only one who's rank is 2 char long
            rank = '10'
            space = ''  # if we write "10" on the card that line will be 1 char to long
        else:
            # some have a rank of 'King' this changes that to a simple 'K' ("King" doesn't fit)
            rank = card.value
            space = ' '  # no "10", we use a blank space to will the void
        # get the cards suit in two steps
        suit = suits_name.index(card.suit)
        suit = suits_symbols[suit]

        # add the individual card on a line by line basis
        lines[0].append('┌─────────┐')
        # use two {} one for char, one for space or char
        lines[1].append('│{}{}       │'.format(rank, space))
        lines[2].append('│         │')
        lines[3].append('│         │')
        lines[4].append('│    {}    │'.format(suit))
        lines[5].append('│         │')
        lines[6].append('│         │')
        lines[7].append('│       {}{}│'.format(space, rank))
        lines[8].append('└─────────┘')

    result = []
    for index, line in enumerate(lines):
        result.append(''.join(lines[index]))
    print('\n'.join(result))


# Statistics & file IO
def write_to_file():
    pass


# Main Menu
def main():
    cls()
    print(WELCOME)
    print(f"{RED}Author: Konrad Bledowski{NO_COLOR}")
    playing = True
    choice = ""
    while playing:
        print("What would you like to do?")
        print("1. Play a game")
        print("2. View statistics")
        print("3. Help")
        print("4. Quit")
        choice = input(" > ")
        if choice == "1":
            cls()
            game()
        elif choice == "2":
            print("Statistics not yet implemented :(")
        elif choice == "3":
            print("Help not yet implemented")
        elif choice == "4":
            playing = False
        else:
            print("Invalid input! Please try again.")

    print("Thank you for using PokerBot. Goodbye")
    sys.exit()


# Function used to debug my program
# test_card_1 = Card('4', 'D')
# test_card_2 = Card('A', 'C')
# test_card_3 = Card('J', 'S')
# test_card_4 = Card('T', 'H')

# print_cards([test_card_1, test_card_2, test_card_3, test_card_4])
def debug_func():
    test_card_1 = Card('A', 'h')
    test_card_2 = Card('2', 'd')
    test_card_3 = Card('9', 's')
    test_card_4 = Card('Q', 'c')
    test_card_5 = Card('4', 'd')
    player_cards = [test_card_1, test_card_2]
    dealer_cards = [test_card_3, test_card_4, test_card_5]
    current_hand(player_cards, dealer_cards)


if __name__ == "__main__":
    main()
    # debug_func()
