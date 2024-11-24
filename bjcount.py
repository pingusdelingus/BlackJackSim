
numLoss = 0
numWins = 0

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
    global count
    #! reshuffles deck if its empty
    if Deck.isEmpty():
        print(f"SHUFFLING CARDS")
        Deck.start()
        count = 0
    
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
    global numLoss, numWins, numDraw
    if playerSum > 21:  # Player busts
        numLoss += 1
    elif dealerSum > 21:  # Dealer busts
        numWins += 1
    elif dealerSum > playerSum:  # Dealer wins
        numLoss += 1
    elif dealerSum < playerSum:  # Player wins
        numWins += 1
    else:  # Draw
        numDraw += 1



hi = [10,11,1]
zero = [7,8,9]
lo = [2,3,4,5,6]

def getCount(cards, currCount):
    global hi, zero, lo
    newCount = currCount
    for c in cards:
        if c.getBJValue() in hi:
            newCount -= 1
        elif c.getBJValue() in lo:
            newCount += 1
        else:
            continue

    return newCount



count = 0
thedeck = Deck()
print(f"SHUFFLING CARDS")
def blackjack():
    global numLoss, numWins, numDraw, hi, zero, lo, count
    human = Player('human')
    dealer = Player('dealer')
    dealCard(human, thedeck)
    dealCard(dealer, thedeck)
    dealCard(human, thedeck)
    dealCard(dealer, thedeck)
    showHandValue(human)
    playerSum = evaluateHandBJ(human)
    dealersum = evaluateHandBJ(dealer)
    print(f"player has: {human.printHand()} ")
    print(f"dealer shows: {dealer.hand[0]}")
    showing = list(human.hand)
    showing += [dealer.hand[0]]
    count = getCount(showing, count)
    print(f"the count is: {count}")
    while playerSum <= 21:

        if playerSum > 21:
            numLoss +=1
            break
        #@======================================================================================
        #~ PLAYER V0
        #~ STANDS IF SUM IS GREATER THAN 14
        #~ HITS OTHERWISE
        if playerSum >= 16:
            usrInput = "S"
        else:
            usrInput = "H"
        #@======================================================================================
                                    
        if usrInput.upper() == "H":
            dealCard(human, thedeck)
            showHandValue(human)
            showing = [human.hand[-1]]
            count = getCount(showing, count)
            print(f"the count is: {count}")
        elif usrInput.upper() == "S":
            showHandValue(dealer)
            dealersum = evaluateHandBJ(dealer)
            while dealersum < 16:
                dealCard(dealer, thedeck)
                showHandValue(dealer)
                dealersum = evaluateHandBJ(dealer)
            showing = list(dealer.hand[1:-1])
            updatedCount = getCount(showing, count)
            print(f"the count is: {count}")
            compare(dealersum,playerSum)
            break
        elif usrInput.upper() == 'Q' or usrInput.upper() == 'X':
            return
        playerSum = evaluateHandBJ(human)
        dealersum = evaluateHandBJ(dealer) 
         


numWins = 0
numLoss = 0
numDraw = 0
def main():
    for _ in range(1000):
    
        blackjack()
        
    print(f"{(numWins) / (numWins + numLoss + numDraw)  }% win rate")
        

main()


