import random
import copy



class Card:
    def __init__(self,value, suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return f"{self.value} of {self.suit}"
    def shortprint(self):
        return f"{self.value}{self.suit}"
    def getSuit(self):
        return self.suit
    def getValue(self):
        return self.value

    def getBJValue(self):
        if self.value == 'A':
            return 11
        if self.value == 'K' or self.value == 'Q' or self.value == 'J':
            return 10
        else:
            return int(self.value)
    def getSuit(self):
        return self.suit
    
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []


class Deck:
    def __init__(self):
        self.numCardsIn = 0
        self.d = []
        self.start()


    def isEmpty(self):
        if self.d is None or len(self.d) == 0:
            return True
        else:
            return False


    def deal(self):
        if self.isEmpty() or self.numCardsIn == 0:
            self.start()
        else:
            self.numCardsIn -= 1
            return self.d.pop()
    
    
    def start(self):
        self.d.clear()
        suits = ['Clubs', 'Hearts', 'Diamonds', 'Spades']
        vals = ['2','3','4','5','6','7','8','9','10','J', 'Q', 'K', 'A']
        for suit in suits:
            for val in vals:
                self.d.append(Card(val,suit))
        random.shuffle(self.d)
        self.numCardsIn = len(self.d)
    def __str__(self):
        return f"Deck with {self.numCardsIn} cards left"
    def uglyprint(self):
        for card in self.d:
            print(card.shortprint(), end=" ")
    def pp(self):
        c = []
        h = []
        d = []
        s = []
        for card in self.d:
            if card.getSuit() == 'Clubs':
                c.append(card)
            if card.getSuit() == 'Hearts':
                h.append(card)
            if card.getSuit() == 'Diamonds':
                d.append(card)
            if card.getSuit() == 'Spades':
                s.append(card)

        lol = [c, h, d, s]
        for index in range(4):
            if index == 0:
                print("Clubs", end = ": ")
                for c in lol[index]:
                    print(c.shortprint(), end = " ")
                print()
            if index == 1:
                print('Hearts', end = ": ")
                for c in lol[index]:
                    print(c.shortprint(), end = " ")
                print()

            if index == 2:
                print("Diamonds", end = ": ")
                for c in lol[index]:
                    print(c.shortprint(), end = ",")
                print()
            if index == 3:
                print("Spades", end = ": ")
                for c in lol[index]:
                    print(c.shortprint(), end = " ")
                print()

class TwoDeck(Deck):
    def __init__(self):
        self.d = []
        self.numCardsIn = 0
        start()
    


    def start(self):

        self.d.clear()
        suits = ['Clubs', 'Hearts', 'Diamonds', 'Spades']
        vals = ['2','3','4','5','6','7','8','9','10','J', 'Q', 'K', 'A']
        for suit in suits:
            for val in vals:
                self.d.append(Card(val,suit))
        random.shuffle(self.d)
        secondDeck = copy.deepcopy(self.d)
        random.shuffle(secondDeck)
        self.d = self.d + secondDeck
        self.numCardsIn = len(self.d) 
        return


