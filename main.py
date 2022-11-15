### Poker Helper Begin Game ###
# This program is designed to help you play poker.
# It will tell you what cards you have and what cards you need to win.

# Ideas: Count number of rounds played, and at the end of the session save the number of rounds played, profit (+/-) to a text file.

from cards import Card
from strategy import *
import sys
import os

player_cards = []
dealer_cards = []

# Main gameplay loop


def game():
    numTurn = 1
    playing = True
    while (numTurn < 4) and playing == True:
        # preflop turn is the first turn
        if numTurn == 1:
            playing = pre_flop()
        # flop occurs on the second turn
        elif numTurn == 2:
            while len(dealer_cards) < 3:
                dealing_cards()
            print_cards(dealer_cards)
            current_hand(player_cards, dealer_cards)
            print("Post-flop turn. What would you like to do?")
            print("1. Call/Raise")
            print("2. Fold")
            choice = input(" >")
            if choice == "2":
                print("You have decided to fold your hand.")
                playing = False
                break
            elif choice == "1":
                print("You have decided to keep playing.")
        else:
            dealing_cards()
            print_cards(dealer_cards)
            current_hand(player_cards, dealer_cards)
        numTurn += 1
    print("This round has concluded, returning to main menu...")


def pre_flop():
    print("You have just been dealt a new hand. Please enter your cards using the following format:")
    print("Ten of Clubs == [Tc]")
    print("Possible card values: 2 3 4 5 6 7 8 9 T J Q K A")
    print("Possible suits: Spades (s), Hearts (h), Clubs (c), Diamonds (d)")
    # add while loop with input validation
    card1 = input("Enter your first card's value and suit >")
    firstCard = Card(card1[0], card1[1])
    card2 = input("Enter your second card's value and suit >")
    secondCard = Card(card2[0], card2[1])
    player_hand1 = ""
    player_hand2 = ""
    suited = "o"
    # os.system('clear')
    print("##################################")
    player_hand1 += firstCard.value
    player_hand1 += secondCard.value
    player_hand1 += suited
    player_hand2 += secondCard.value
    player_hand2 += firstCard.value
    player_hand2 += suited
    print_cards([firstCard, secondCard])
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
    player_cards.append(firstCard)
    player_cards.append(secondCard)
    print("##################################")
    print("Pre-flop turn. What would you like to do?")
    print("1. Call/Raise")
    print("2. Fold")
    choice = input(" >")
    if choice == "1":
        print("You have decided to keep playing.")
        return True
        # Player now enters 3 flop cards for calculation
    elif choice == "2":
        print("You have decided to fold your hand.")
        return False
        # update stats and return to main menu

# Dealing a card to the table


def dealing_cards():
    print("The dealer has dealt a card to the table! Please enter the card's value and suit in the following format:")
    print("Ten of Clubs == [Tc]")
    ask = input(" >")
    dealt_card = Card(ask[0], ask[1])
    dealer_cards.append(dealt_card)

# Printing ASCII version of playing cards


def print_cards(cards):
    suits_name = ['s', 'd', 'h', 'c']
    suits_symbols = ['♠', '♦', '♥', '♣']
    lines = [[] for i in range(9)]
    for index, card in enumerate(cards):
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


def statistics():
    pass

# Main Menu


def main():
    print("Welcome to PokerBot 1.0.0")
    print("Author: Konrad Bledowski")
    # test_card_1 = Card('4', 'D')
    # test_card_2 = Card('A', 'C')
    # test_card_3 = Card('J', 'S')
    # test_card_4 = Card('T', 'H')

    # print_cards([test_card_1, test_card_2, test_card_3, test_card_4])
    playing = True
    choice = ""
    while playing:
        print("What would you like to do?")
        print("1. Play a game")
        print("2. View statistics")
        print("3. Quit")
        choice = input(" > ")
        if choice == "1":
            print("Starting game...")
            game()
        elif choice == "2":
            print("Statistics not yet implemented :(")
        elif choice == "3":
            playing = False
        else:
            print("Invalid input! Please try again.")

    print("Thank you for using PokerBot. Goodbye")
    sys.exit()


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
    # main()
    debug_func()
