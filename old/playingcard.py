import random


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return f"{self.value} of {self.suit}"
    def getCardValue(self):
        if self.value == "J" or self.value == "Q" or self.value == "K":
            return 10
        else:
            return self.value

#------------------------------------------------------------------
#------------------------------------------------------------------

class Deck:
    def __init__(self):
        self.d = []
        self.shuffle()
#------------------------------------------------------------------

    def shuffle(self):
        #empty out the deck if contains card objects
        self.d.clear()
        suits = ['Clubs', 'Hearts', 'Diamonds', 'Spades']
        vals = ['2','3','4','5','6','7','8','9','10','J', 'Q', 'K', 'A']
        for suit in suits:
            for val in vals:
                self.d.append(Card(val,suit))
        #shuffles cards after being appended to the end of the deck in order 
        #! maybe we can add randomly from the lists and then pop and pick randomly to speed up games... 
        # TODO!
        #
        #
        # using built in method to shuffle array, can be improved
        random.shuffle(self.d)
    

    # returns a list of 2 items, that are card objects
    def deal_blackjack(self):
        if len(self.d) == 0:
            print("deck is empty, adding cards and shuffling")
            self.shuffle()
        else:
            return self.d.pop()
    def deal_poker_player(self)
        if len(self.d ==0):
            print("empty deck, adding cards and shuffling")
            self.shuffle()
        return [self.d.pop(), self.d.pop()]
#------------------------------------------------------------------
    # toString for deck of cards
    def __str__(self):
        return f"This is a deck with {len(self.d)} cards currently!"

    

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    def getCard(self, index):
        if self.hand is not None:
            return self.hand[index]
    def __str__(self):
        return f"This is {self.name} and they have in their hand: {self.hand}"
    def emptyHand(self):
        print(f" cleaing {self.name}'s hand")
        self.hand.clear()
    def showDealerCards(self):
        return f"{self.hand[0]}, {self.hand[1]}"
