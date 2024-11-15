import random


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return f"{self.value} of {self.suit}"
    def getCard(self, index):
        if self.value == "J" or self.value == "Q" or self.value == "K":
            return 10
        else:
            return self.value

#------------------------------------------------------------------
#------------------------------------------------------------------

class Deck:
    def __init__(self):
        # 2d array of suits, then vals 
        self.d = []
        self.suits =  ['Clubs', 'Hearts', 'Diamonds', 'Spades']
        self.values = ['2','3','4','5','6','7','8','9','10','J', 'Q', 'K', 'A']
 
        self.openDeck()
    def deal_random(self):
        return self.d.pop()
#------------------------------------------------------------------
    def prettyprint(self):
        # Print header row with values
        print("     " + "  ".join(self.values))
        print("    " + "-" * (len(self.values) * 3))

        # Print each row with "X" if the card is present
        for i, suit in enumerate(self.suits):
            row = [f"{suit[:7]:<7}"]  # Format suit to a width of 7 characters
            for card in self.values:
                # Check if the card exists in the current suit list
                if any(c.value == card for c in self.d[i]):
                    row.append("X")
                else:
                    row.append(" ")
            print("  ".join(row))   

    def openDeck(self):
        #empty out the deck if contains card objects
        self.d.clear()
        self.d = [[] for _ in range(4)]
        suits = ['Clubs', 'Hearts', 'Diamonds', 'Spades']
        vals = ['2','3','4','5','6','7','8','9','10','J', 'Q', 'K', 'A']
        for index, suit in enumerate(suits):
            for val in vals:
                self.d[index].append(Card(val, suit))


                
        #shuffles cards after being appended to the end of the deck in order 
        #! maybe we can add randomly from the lists and then pop and pick randomly to speed up games... 
        # TODO!
    


    def deal_blackjack(self):
        if len(self.d) == 0:
            print("deck is empty, adding cards and shuffling")
            self.shuffle()
        else:
            return self.d.pop()

#------------------------------------------------------------------
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
