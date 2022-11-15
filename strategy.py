import itertools

hand_values = {
    1: "High card",
    2: "One pair",
    3: "Two pair",
    4: "Three of a kind",
    5: "Straight",
    6: "Flush",
    7: "Full house",
    8: "Four of a kind",
    9: "Straight flush"
}

card_values = {
    14: "Ace",  # value of the ace is high until it needs to be low
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Jack",
    12: "Queen",
    13: "King"
}

all_possible_cards = ['2s', '2h', '2d', '2c', '3s', '3h', '3d', '3c', '4s', '4h', '4d', '4c', '5s', '5h', '5d', '5c', '6s', '6h', '6d', '6c', '7s', '7h', '7d', '7c', '8s',
                      '8h', '8d', '8c', '9s', '9h', '9d', '9c', 'Ts', 'Th', 'Td', 'Tc', 'Js', 'Jh', 'Jd', 'Jc', 'Qs', 'Qh', 'Qd', 'Qc', 'Ks', 'Kh', 'Kd', 'Kc', 'As', 'Ah', 'Ad', 'Ac']

#possible_hands = list(itertools.combinations(all_possible_cards, 5))

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


# used to determine the best hand that the player currently has
# use itertools to create all possible variations of the hand the player has, and then find the highest value 5 card combination
def current_hand(player_cards, dealer_cards):
    best_hand = []
    value = 1  # priority 1
    high_card = 0  # priority 2
    pd_cards = player_cards + dealer_cards
    pd_card_values = []
    for card in pd_cards:
        pd_card_values.append(card.points)
    possible_hands = list(itertools.combinations(pd_cards, 5))
    for possible_hand in possible_hands:
        if calculate_best(possible_hand, pd_card_values) > value:
            value = calculate_best(possible_hand, pd_card_values)
            high_card = find_high_card(pd_card_values)
            best_hand = possible_hand
        elif value == 1:
            high_card = find_high_card(pd_card_values)

    print("You currently have a " + hand_values[value] + "!")
    print("Your high card is a(n): ", card_values[high_card])
    print("This hand has a value of:", value,
          "out of 9, where 1 is the weakest and 9 is the strongest.")


def calculate_best(possible_hand, pd_card_values):
    print("These are your cards vals: " + str(pd_card_values))
    value = 0
    if (contains_straight(pd_card_values) and contains_flush(possible_hand)):  # Covers straight flush
        return 9
    # Covers 4 of a kind and full house [7,8]
    elif (find_x_of_a_kind(pd_card_values) >= 7):
        return find_x_of_a_kind(pd_card_values)
    # Covers flush
    elif (contains_flush(possible_hand)):
        return 6
    # Covers straight
    elif (contains_straight(pd_card_values)):
        return 5
    # Covers high card, one pair, two pair, three of a kind [1,2,3,4]
    else:
        return find_x_of_a_kind(pd_card_values)


# Example all_card_values = [2,4,5,5,7,11,12]
# High card = 1 [done]
# One Pair = 2 [done]
# Two Pair = 3 [done]
# Three of a kind = 4 [done]
# Straight = 5 [done]
# Flush = 6 [done]
# Full House = 7 [done]
# 4 of a kind = 8 [done]
# Straight Flush = 9 [done]


# Convert the while loop to a for loop later, wouldn't need counter anymore
def contains_straight(all_card_values):
    straight_values = all_card_values.copy()
    straight = False
    if 14 in straight_values:
        straight_values.append(1)
    straight_values.sort()
    straight_values.reverse()
    prev = 0
    counter = 1
    consecutive_nums = 1
    while counter < len(straight_values):
        if consecutive_nums == 5:
            break
        if (straight_values[counter]) == (straight_values[prev] - 1):
            consecutive_nums += 1
        else:
            consecutive_nums = 1

        counter += 1
        prev += 1
    if consecutive_nums >= 5:
        straight = True
    return straight


def contains_flush(all_cards):
    flush = False
    diamonds, spades, clubs, hearts = 0, 0, 0, 0
    for card in all_cards:
        if card.suit == 'd':
            diamonds += 1
        elif card.suit == 's':
            spades += 1
        elif card.suit == 'c':
            clubs += 1
        else:
            hearts += 1
    if (diamonds >= 5 or spades >= 5 or clubs >= 5 or hearts >= 5):
        flush = True
    return flush


def find_x_of_a_kind(all_card_values):
    num_of_kind = 0
    num_pairs = 0
    frequency = {}
    # iterating over the list
    for num in all_card_values:
        # checking the element in dictionary
        if num in frequency:
            # incrementing the counr
            frequency[num] += 1
        else:
            # initializing the count
            frequency[num] = 1
    for num in frequency:
        if frequency[num] == 2:
            num_pairs += 1
        if frequency[num] > num_of_kind:
            num_of_kind = frequency[num]
    if num_of_kind == 4:  # Four of a kind
        return 8
    elif num_of_kind == 3 and num_pairs == 1:  # Full House
        return 7
    elif num_of_kind == 3:  # 3 of a kind
        return 4
    elif num_pairs == 2:  # 2 pair
        return 3
    elif num_pairs == 1:
        return 2
    else:
        return 1


def find_high_card(values):
    return max(values)
