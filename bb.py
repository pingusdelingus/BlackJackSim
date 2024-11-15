import random
from colorama import Fore, Style
from colorama import init
init(autoreset=True)
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
    cards =""
    for c in Player.hand:
        cards += f"{c.shortprint()}, "

    print(f"{Player.name} has a hand: {cards} with value {val}")


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

def compare(playerSum, dealerSum):
    if playerSum > 21:
            print(f"{Fore.RED} Player busts with {playerSum} {Style.RESET_ALL}")
    elif dealerSum > 21:
        print(f" {Fore.GREEN} Player wins with {playerSum} {Style.RESET_ALL}")
    elif dealerSum == playerSum:
        print(f"Tie: Player and dealer both have {playerSum}")
    elif dealerSum > playerSum:
        print(f"{Fore.RED} Dealer wins with {dealerSum} against player's {playerSum} {Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN} Player wins with {playerSum} against dealer's {dealerSum} {Style.RESET_ALL}")
    #if playerSum > 21 and dealerSum <= 21:
    #    print(f"player busts with {playerSum}")
    #    exit
    #if dealerSum > 21 and playerSum <= 21:
    #    print(f"player wins with {playerSum}")
    #    exit
    #if dealerSum == 21 and playerSum == 21:
    #    print(f"tie both with {playerSum}")
    #    exit
    #if dealerSum < 21 and playerSum < 21 and dealerSum > playerSum:
    #    print(f"dealer wins with {dealerSum} againt human's {playerSum}")
    #    exit

    #if dealerSum < 21 and playerSum < 21 and playerSum > dealerSum:
    #    print(f"player wins with {playerSum} against the dealer's {dealerSum}")
    #    exit

    #if dealerSum < 21 and playerSum < 21 and playerSum == dealerSum:
    #    print(f"player and dealer tie with {playerSum}")
    #    exit
    #else:
    #    print('error in comapre method')

thedeck = Deck()
def blackjack():
    validOptions = ['h',  's', 'k', 'q']
    human = Player('human')
    dealer = Player('dealer')
    firstDeal(human, dealer, thedeck)
    showHandValue(human)
    playerSum = evaluateHandBJ(human)
    dealersum = evaluateHandBJ(dealer)

    while playerSum <= 21:
        print(f"The dealer is showing a {dealer.hand[0]}")
        usrInput = input("What would you like to do? (H)it |  (S)tand | (K)Surrender | or e(X)it:")
        while usrInput.lower() not in validOptions:
            usrInput = input("What would you like to do? (H)it |  (S)tand | (K)Surrender | or e(X)it:")
            
        if usrInput.upper() == "H":
            dealCard(human, thedeck)
            showHandValue(human)
        elif usrInput.upper() == "S":
            showHandValue(dealer)
            dealersum = evaluateHandBJ(dealer)
            while dealersum <= 16:
                dealCard(dealer, thedeck)
                showHandValue(dealer)
                dealersum = evaluateHandBJ(dealer)
            compare(playerSum,dealersum)
            break
        elif usrInput.upper() == "K":
            print("Surrendering hand")
            ourDealer.emptyHand()
            ourPlayer.emptyHand()
        elif usrInput.upper() == 'X' or 'Q':
            exit()

        playerSum = evaluateHandBJ(human)
        dealersum = evaluateHandBJ(dealer) 
    if playerSum > 21:
        print(f"{Fore.RED} player busts with {playerSum}")

while not thedeck.isEmpty():
    blackjack()
    print("Dealing new hand...")
    print("- " * 100)






