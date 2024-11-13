import random

from pc import *

#black jack functions

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

# take in a player object,  and evaluate their hand (sum) and returns it
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

def showHandValue(Player):
    val = evaluateHandBJ(Player)
    print(f"{Player.name} has a hand: {Player.hand} with value {val}")


# deal to person
def dealCard(person, Deck):
    person.hand.append(Deck.deal())

def firstDeal(Player, Dealer, Deck):
    for index in range(2):
        dealCard(Player, Deck)
        dealCard(Dealer, Deck)
def flipDealerCards(Player, Deck, Dealer):
    dealerValue = evaluateHandBJ(Dealer)
    showHandValue(Dealer)
    if dealerValue >= 17:
        print('dealer stands, comparing hands')
    while(dealerValue < 17):
        if dealerValue > 21:
            print('dealer busts')
        dealCard(Dealer, Deck)
        dealerValue = evaluateHandBJ(Dealer)
        showHandValue(Dealer)
    

human = Player('human')
dealer = Player('dealer')
thedeck = Deck()
firstDeal(human, dealer, thedeck)
showHandValue(human)


print(f"The dealer is showing a {dealer.hand[0]}")

usrInput = input("What would you like to do? (H)it |  (S)tand | (K)Surrender | or e(X)it:")
while usrInput not in validOptions:
    usrInput = input("What would you like to do? (H)it |  (S)tand | (K)Surrender | or e(X)it:")
    
if usrInput.upper() == "H":
    dealCard(ourPlayer, ourDeck)
elif usrInput.upper() == "S":
    dealersum = flipDealerCards(ourPlayer, ourDeck, ourDealer)
    compare()
elif usrInput.upper() == "K":
    print("Surrendering hand")
    ourDealer.emptyHand()
    ourPlayer.emptyHand()













