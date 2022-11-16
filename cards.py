# cards

class Card(object):
    card_values = {
        'A': 14,  # value of the ace is high until it needs to be low
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        '?': 0
    }

    def __init__(self) -> None:
        self.value = "none"
        self.suit = "none"
        self.points = "none"

    def __init__(self, value, suit):
        """
        :param suit: The face of the card, e.g. Spade or Diamond
        :param value: The value of the card, e.g 3 or King
        :param points: Numerical power of given card value, ie: 10 is worth 10 points, J is worth 11.
        """
        self.value = value
        self.suit = suit
        self.points = self.card_values[value]

    def setValue(self, value):
        self.value = value

    def setSuit(self, suit):
        self.suit = suit

    def getValue(self):
        return self.value

    def getSuit(self):
        return self.suit

    def getPoints(self):
        return self.points

    def printCard(self):
        print("This card is a(n) %s of %s", self.value, self.suit)
