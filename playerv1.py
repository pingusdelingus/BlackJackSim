
numLoss = 0
numWins = 0

cardCount = 0

chips = 1000

bets = {'s': 10, 'm' :25 , 'b' : 100}

from colorama import Fore, Style
from colorama import init
from pc import *

init(autoreset=True)


# take in a player object, and evaluates their hand (sum) and returns it
def evaluateHandBJ(Player: Player) -> int:
    h = Player.hand
    checkAce = 0
    sum = 0
    
    # go through each card in hand
    for card in h:
        if card is None:
            # print("Error hand contains a NONE card.")
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
                # print('error in evaluateHandBJ')
                return
            if sum + 11 <= 21:
                # print('counting ace as 11')
                sum = sum + 11
            elif sum + 11 > 21 and sum + 1 <= 21:
                # print('counting ace as 1')
                sum = sum + 1
            checkAce -=1 
            
        return sum


def showHandValue(Player: Player):
    val = evaluateHandBJ(Player)
    cards = ""
    for c in Player.hand:
        cards += f"{c.shortprint()}, "

    # print(f"{Player.name} has a hand: {cards} with value {Fore.RED}{val}")


# deal to person
def dealCard(person: Player, Deck: Deck):
    #! reshuffles deck if its empty
    if Deck.isEmpty():
        Deck.start()
        cardCount = 0
    
    person.hand.append(Deck.deal())


def firstDeal(Player: Player, Dealer: Player, Deck: Deck):
    for _ in range(2):
        dealCard(Player, Deck)
        dealCard(Dealer, Deck)


def flipDealerCards(Deck: Deck, Dealer: Player):
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

# compare the hands of the dealer and player
def compare(dealerSum, playerSum):
   
    global numLoss, numWins, numTie
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

def updateCount(player):
    lo = [2,3,4,5,6]
    c = player.hand[-1]
    if c.getValue() == 10 or c.getValue() == 11 or c.getValue() == 1:
        count -= 1
    elif c.getValue() in lo:
        count += 1
    return
    
    
thedeck = Deck()
thedeck.start()
def blackjack():
    zeroes = [7,8,9]
    lo = [2,3,4,5,6]
    global numLoss, numWins
    human = Player('human')
    dealer = Player('dealer')
    dealCard(human, thedeck)
    dealCard(dealer, thedeck)
    dealCard(human, thedeck)
    dealCard(dealer, thedeck)
    showHandValue(human)
    dealerTopCard = dealer.hand[0].getBJValue()
    playerSum = evaluateHandBJ(human)
    dealersum = evaluateHandBJ(dealer)
    
    firstThreeCards = []
    firstThreeCards.append(human.hand[0])
    firstThreeCards.append(human.hand[1])

    firstThreeCards.append( dealer.hand[0])
    
    
    for c in firstThreeCards:
        if c.getValue() == 10 or c.getValue() == 11 or c.getValue() == 1:
            count -= 1
        elif c.getValue() in lo:
            count += 1

    while playerSum <= 21:
        #@======================================================================================
        #~ PLAYER V1
        #~ stand or hit based on card count
        #~ count - 1 -> [10, J, Q, K, A]
        #~ count + 1 -> [2, 3, 4, 5, 6]
        #~ do nothing on [7, 8, 9]

        #~ low count => more low cards
        #~ high count => more high cards
        #@======================================================================================
        
        hasAce = False
        usrInput = ""
        for c in human.hand:
            if c.getValue() == 11 or c.getValue() == 1:
                hasAce = True
                
        
        if cardCount >= 2:
            if (12 <= playerSum and playerSum <= 16) and (dealerTopCard == 10 or dealerTopCard == 11 or dealerTopCard == 1):
                usrInput = "S"
            elif playerSum == 16 and dealerTopCard in zeroes:
                usrInput = "S"
            elif playerSum == 17 and hasAce:
                usrInput = "S"
            elif playerSum < 12:
                usrInput = "H"
            elif playerSum >= 17:
                usrInput = "S"
        elif cardCount <= -1:
            if playerSum == 12 and dealerTopCard in lo:
                usrInput = "H"
            elif playerSum == 16 and not hasAce:
                if dealerTopCard >= 7:
                    usrInput = 'H'
                
            elif playerSum == 11 or playerSum == 10:
                usrInput = "H"
            elif playerSum == 15 or playerSum == 16 and dealerTopCard >= 7 and not hasAce:
                usrInput = "H"
            elif playerSum == 13 or playerSum == 14:
                usrInput = 'H'
            elif playerSum < 10:
                usrInput = "H"
            elif playerSum > 16:
                usrInput = 'S'
            
        else:
            if (12 <= playerSum and playerSum <= 16) and (7 <= dealerTopCard <= 11 ):
                usrInput = "H"
            elif playerSum < 12:
                usrInput = 'H'
            elif (12 <= playerSum and playerSum <= 16) and (2 <= dealerTopCard <= 6 ):
                usrInput = "S"
            elif (playerSum >= 17 and not hasAce):
                usrInput = "S"
            elif ( 13 <= playerSum <= 18) and dealerTopCard in lo and not hasAce:
                #! double down if allowed, else hit
                usrInput = "H"
            elif ( 13 <= playerSum <= 18) and (7 <= dealerTopCard <= 11 )and not hasAce:
                usrInput = "H"
            
            elif playerSum >= 19 and hasAce:
                usrInput = "S"
            
            
        

        
        
        if usrInput.upper() == "H":
            dealCard(human, thedeck)
            updateCount(human)
            showHandValue(human)
        elif usrInput.upper() == "S":
            showHandValue(dealer)
            dealersum = evaluateHandBJ(dealer)
            while dealersum < 16:
                dealCard(dealer, thedeck)
                updateCount(dealer)
                showHandValue(dealer)
                dealersum = evaluateHandBJ(dealer)
            compare(dealersum,playerSum)
            break
        elif usrInput.upper() == 'Q' or usrInput.upper() == 'X':
            return
        playerSum = evaluateHandBJ(human)
        dealersum = evaluateHandBJ(dealer) 
    if playerSum > 21:
        numLoss +=1
         


numWins = 0
numLoss = 0
numTie = 0
def main():
    for _ in range(1000):
    
        blackjack()
        
    print(f"{(numWins / (numLoss + numWins) )  }% win rate")
        

main()


