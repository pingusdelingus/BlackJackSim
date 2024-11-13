import random

from pc import *

#black jack functions

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

# take in a player object, currentHandValue and evaluate their hand
def evaluateHandBJ(Player ):
    h = Player.hand
    checkAce = 0
    sum = 0
    for card in h:
        if card.getBJValue() == 11:
            checkAce += 1
        else:
            sum += card.getBJValue()
    if checkAce == 0:
        return sum 
    else:
        while(checkAce != 0):
            if checkAce < -10 or checkAce > 10:
                print('error in evaluateHandBJ')
                return
            if sum + 11 <= 21:
                print('counting ace as 11')
                sum = sum + 11
            elif sum + 11 > 21 and sum + 1 <= 21:
                print('counting ace as 1')
                sum = sum + 1
            checkAce -=1 
        return sum
    print('how tf did this code execute')




# deal to person
def dealCards(person, Deck):
    person.hand.append(Deck.deal())

def firstDeal(Player, Dealer, Deck):
    for index in range(2):
        dealCards(Player, Deck)
        dealCards(Dealer, Deck)




