# cards

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def setValue(self, value):
        self.value = value

    def setSuit(self, suit):
        self.suit = suit

    def getValue(self):
        return self.value

    def getSuit(self):
        return self.suit

    def printCard(self):
        print("This card is a(n) %s of %s", self.value, self.suit)
