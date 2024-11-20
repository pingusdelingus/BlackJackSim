numLoss = 0
numWins = 0
import random
from colorama import Fore, Style
from colorama import init
init(autoreset=True)
from pc import *
def dealCard(person, Deck):
    person.hand.append(Deck.deal())
#black jack functions
# take in a player object,  and evaluate their hand (sum) and returns it
def evaluateHandBJ(Player ):
    h = Player.hand
    checkAce = 0
    sum = 0
    for card in h:
        if card is None:
            print("Error hand contains a NONE card.")
            return 0
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
    cards = ""
    for c in Player.hand:
        cards += f"{c.shortprint()}, "

    print(f"{Player.name} has a hand: {cards} with value {Fore.RED}{val}")


# deal to person

def firstDeal(Player, Dealer, Deck):
    for index in range(2):
        checkShuffle(Player, Deck)
        checkShuffle(Dealer, Deck)



def flipDealerCards(Player, Deck, Dealer):
    dealerValue = evaluateHandBJ(Dealer)
    showHandValue(Dealer)
    if dealerValue >= 17:
        print('dealer stands, comparing hands')
    while(dealerValue < 17):
        if dealerValue > 21:
            print('dealer busts')
        checkShuffle(Dealer, Deck)
        dealerValue = evaluateHandBJ(Dealer)
        showHandValue(Dealer)

def compare(dealerSum, playerSum):
    global numLoss, numWins
    if playerSum > 21:
        print(f"{Fore.RED} Player busts with {playerSum} {Style.RESET_ALL}")
        numLoss +=1
        #numLoss +=1
    elif dealerSum > 21:
        print(f" {Fore.GREEN} Player wins with {playerSum} {Style.RESET_ALL}")
        numWins += 1
        #numWins +=1 
    elif dealerSum == playerSum:
        print(f"Tie: Player and dealer both have {playerSum}")

    elif dealerSum > playerSum:
        print(f"{Fore.RED} Dealer wins with {dealerSum} against player's {playerSum} {Style.RESET_ALL}")
        numLoss +=1
        #numLoss +=1
    else:
        print(f"{Fore.GREEN} Player wins with {playerSum} against dealer's {dealerSum} {Style.RESET_ALL}")
        numWins +=1 
        #numWins += 1
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
def checkShuffle(player, deck):

    if len(thedeck.d) > 0:
        dealCard(player, deck)
    else:
        print("deck out of cards! shuffling now")
        deck.start()
        dealCard(player,deck)



thedeck = Deck()
thedeck.start()
def blackjack():
    global numLoss, numWins
    validOptions = ['h', 's', 'k', 'q', 'x']
    human = Player('human')
    dealer = Player('dealer')
    checkShuffle(human, thedeck)
    checkShuffle(dealer, thedeck)
    checkShuffle(human, thedeck)
    checkShuffle(dealer, thedeck)
    showHandValue(human)
    playerSum = evaluateHandBJ(human)
    dealersum = evaluateHandBJ(dealer)

    while playerSum <= 21:
        print(f"The dealer is showing a {dealer.hand[0]}")
        usrInput = input("What would you like to do? (H)it |  (S)tand | (K)Surrender | or e(X)it:")
        while usrInput.lower() not in validOptions:
            usrInput = input("What would you like to do? (H)it |  (S)tand | (K)Surrender | or e(X)it:")
            
        if usrInput.upper() == "H":
            checkShuffle(human, thedeck)
            showHandValue(human)
        elif usrInput.upper() == "S":
            showHandValue(dealer)
            dealersum = evaluateHandBJ(dealer)
            while dealersum < 16:
                checkShuffle(dealer, thedeck)
                showHandValue(dealer)
                dealersum = evaluateHandBJ(dealer)
            compare(dealersum,playerSum)
            break
        elif usrInput.upper() =="X":
            print('goodbye')
            exit()
        elif usrInput.upper() == "K":
            print("Surrendering hand")
            ourDealer.emptyHand()
            ourPlayer.emptyHand()
            numLoss +=1
            return
        elif usrInput.upper() == 'Q' or usrInput.upper() == 'X':
            print("game ending... goodbye!")
            return
        playerSum = evaluateHandBJ(human)
        dealersum = evaluateHandBJ(dealer) 
    if playerSum > 21:
        print(f"{Fore.RED} player busts with {playerSum}")
        numLoss +=1
         


numWins = 0
numLoss = 0
numTie = 0

chips = 1000
def main():
    valid = ['Y', 'N']
    while not thedeck.isEmpty():
        print('Dealing new cards...')
        print('-' * 100)
        blackjack( )
    usrInput = input("Would you like to play again? (Y/N)")
    while usrInput.upper() not in valid:
        usrInput = input("Would you like to play again? (Y/N)")
    if usrInput.upper() == 'Y':
        thedeck.start()
        main()
    else:
        exit()
main()


