### Poker Helper Begin Game ###
# This program is designed to help you play poker.
# It will tell you what cards you have and what cards you need to win.

# Ideas: Count number of rounds played, and at the end of the session save the number of rounds played, profit (+/-) to a text file.

from cards import Card
import sys
import itertools
import os

cards = ['2s', '2h', '2d', '2c', '3s', '3h', '3d', '3c', '4s', '4h', '4d', '4c', '5s', '5h', '5d', '5c', '6s', '6h', '6d', '6c', '7s', '7h', '7d', '7c', '8s',
         '8h', '8d', '8c', '9s', '9h', '9d', '9c', 'Ts', 'Th', 'Td', 'Tc', 'Js', 'Jh', 'Jd', 'Jc', 'Qs', 'Qh', 'Qd', 'Qc', 'Ks', 'Kh', 'Kd', 'Kc', 'As', 'Ah', 'Ad', 'Ac']

possible_hands = itertools.combinations(cards, 5)

STier = ['AAo', 'AKs', 'AQs', 'AJs', 'ATs', 'A9s',
         'A8s', 'A7s', 'A6s', 'A5s', 'A4s', 'A3s', 'A2s', 'AKo',
         'KKo', 'KQs', 'KJs', 'KTs', 'AQo', 'KQo', 'QQo', 'QJs', 'QTs', 'AJo',
         'JJo', 'JTs', 'ATo', 'TTo', 'T9s', '99o', '88o', '77o', '66o', '65s', '55o']

ATier = ['KJo', 'QJo', 'K9s', 'K8s', 'Q9s',
         'J9s', '98s', '87s', '76s', '54s', '44o']

BTier = ['KTo', 'QTo', 'JTo', 'K7s', 'K6s', 'K5s', 'Q8s',
         'J8s', 'T8s', '97s', '86s', '75s', '33o', '22o']

CTier = ['K4s', 'K3s', 'K2s', 'Q7s', 'Q6s', 'Q5s', 'J7s', 'T7s', 'T6s', 'A9o', 'K9o', 'Q9o',
         'J9o', 'T9o', 'A8o', '98o', '96s', '85s', 'A7o', 'A6o', 'A5o', 'A4o', '64s', '53s', '43s']

DTier = ['Q4s', 'Q3s', 'Q2s', 'J6s', 'J5s', 'J4s', 'J3s', 'J2s', 'T5s', 'T4s', 'T3s', 'T2s', '95s', '94s', '84s', 'K8o', 'Q8o', 'J8o', 'T8o', 'K7o', 'Q7o',
         'J7o', 'T7o', '97o', '87o', '74s', '73s', 'K6o', 'Q6o', '86o', '76o', '63s', 'K5o', 'Q5o', '75o', '65o', '52s', 'K4o', '64o', '54o', '42s', 'A3o', '32s', 'A2o']


def poker_hand():
    print("You have just been dealt a new hand. Please enter your cards using the following format:")
    print("Ten of Clubs == [Tc]")
    print("Possible card values: 2 3 4 5 6 7 8 9 T J Q K A")
    print("Possible suits: Spades (s), Hearts (h), Clubs (c), Diamonds (d)")
    card1 = input("Enter your first card's value and suit >")
    firstCard = Card(card1[0], card1[1])
    card2 = input("Enter your second card's value and suit >")
    secondCard = Card(card2[0], card2[1])
    player_hand1 = ""
    player_hand2 = ""
    suited = "o"
    os.system('clear')
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
        print("Suggested play: fold, unless you're going last. Examine how the other players are betting pre-flop.")
    elif (player_hand1 in DTier) or (player_hand2 in DTier):
        print("Your hand is awful. [D Tier]")
        print("Suggested play: Fold preflop. Only play this hand as a small blind.")
    else:
        print("Your hand is trash!")
        print("Suggested play: fold immediately.")
    if firstCard.suit == secondCard.suit:
        suited = "s"
        print("NOTE: Your cards are suited! Watch for a possible flush draw.")
    print("##################################")
    print("Pre-flop turn. What would you like to do?")
    print("1. Call/Raise")
    print("2. Fold")
    choice = input(" >")
    if choice == "1":
        print("You have decided to keep playing.")
        # Player now enters 3 flop cards for calculation
    elif choice == "2":
        print("You have folded. Thank you for using PokerBot")
        # update stats and return to main menu


def pre_flop():
    print("Pre-flop turn. What would you like to do?")
    print("1. Call/Raise")
    print("2. Fold")
    choice = input(" >")
    if choice == "1":
        print("You have decided to keep playing.")
        # Player now enters 3 flop cards for calculation
    elif choice == "2":
        print("You have decided to fold your hand. Thank you for using PokerBot")
        # update stats and return to main menu


def print_cards(cards):
    suits_name = ['S', 'D', 'H', 'C']
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


def main():
    print("Welcome to PokerBot 1.0.0")
    print("Author: Konrad Bledowski")

    print("What would you like to do?")
    print("1. Play a game")
    print("2. View statistics")
    print("3. Quit")
    # test_card_1 = Card('4', 'D')
    # test_card_2 = Card('A', 'C')
    # test_card_3 = Card('J', 'S')
    # test_card_4 = Card('T', 'H')

    # print_cards([test_card_1, test_card_2, test_card_3, test_card_4])
    choice = input(" > ")
    if choice == "1":
        print("Starting game...")
        poker_hand()
    elif choice == "2":
        print("Statistics not yet implemented :(")
    elif choice == "3":
        print("Thank you for using PokerBot. Goodbye")
        sys.exit()


main()
