from playingcard import *
import copy



#returns a list of the total sums of the cards in a players hand, either dealer or players
def calculateHand(Player):
    currHand = Player.hand
    for index in range(len(currHand)):
        if currHand[index] in faceCards:
            currHand[index] = 10
        elif currHand[index] == 'A':
            currHand[index] = 'w':
        else:
            currHand[index] = int(currHand[index])
    if 'w' in currHand:
        second = copy.deepcopy(currHand)
        for index in range(len(currHand)):
            if currHand[index] == 'w':
                currHand[index] = 1
                second[index] = 11
        return ['A', sum(second), sum(currHand)]
    else:
        return ['56', sum(currHand)]


#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------

def hitPlayer(Player, Deck):
    nextCard = Deck.deal_blackjack()
    Player.hand.apend(nextCard)
    newTotal = calculateHand(Player)
    if newTotal[0] == 56:
        return newTotal[1]
    else:
        if newTotal[1] > 21 and newTotal[2] <= 21
            return newTotal[2]
        if newTotal[1] <= 21 and newTotal[2] > 21:
            return newTotal[1]
        if newTotal[1] <= 21 and newTotal[2] <= 21:
            return ['A', newTotal[1], newTotal[2]]
    print("error in hitplayer method")
    return -1
#--------------------------------------------------------------------------------------------
def hit(Player,Deck):
    res = hitPlayer(ourPlayer, ourDeck)
    if res[0] == "A":
        userInput = input(f" choose either : {res[1]} or : res{2}, enter either 1 or 2:")
        while userInput not in ['1', '2']
            userInput = input(f" choose either : {res[1]} or : res{2}, enter either 1 or 2:")
        if userInput == '1':
            res = res[1]
        else:
            res = res[2]
    else:
        res = res[0]
    return res



def flipDealerCards(Player, Deck, Dealer, dealersum):
    print("no more bets.. flipping dealer cards:")
    print(f"The dealers cards are: {Dealer.showDealerCards()}")
    while dealersum <= 16:
        dealersum = hit(Dealer, Deck)
    return dealersum

     
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------

def main():
    ourDeck = Deck()
    faceCards = ['J', 'Q', 'K']
    validOptions = ['X', 'x', 'H', 'h', 'K', 'k', 'S', 's']
#checking constructor and making sure that toString works!
    print(ourDeck)

    print("Welcome to 1-Handed BlackJack")
    ourDealer = Player("Dealer") 
    ourPlayer = Player("Human")
    for index in range(2):
        ourDealer.hand.append(ourDeck.deal_blackjack()) 
        ourPlayer.hand.append(ourDeck.deal_blackjack())
    dealerSum = calculateHand(ourDealer)
    playerSum = calculateHand(ourPlayer)





    # GAME LOOP
    while len(ourDeck.d) != 0 and playerSum <= 21 and dealerSum <= 21:
        
        print(f"{ourPlayer} and your total is {playerSum}")
        print(f"The dealer is showing a {ourDealer.hand[0]}")
        print("What would you like to do? (H)it |  (S)tand | (K)Surrender | or e(X)it:")



        usrInput = input("") 
        while usrInput not in validOptions:
            print("What would you like to do? (H)it |  (S)tand | (K)Surrender | or e(X)it:")
            usrInput = input("") 
        
        if usrInput.upper() == "H":
            playerSum = hit(ourPlayer, ourDeck)
        elif userInput.upper() == "S":
            dealersum = flipDealerCards(ourPlayer, ourDeck, ourDealer, dealerSum)
        elif userInput.upper() == "K":
            print("Surrendering hand")
            ourDealer.emptyHand()
            ourPlayer.emptyHand()
        

        if playerSum > 21:
            print("Player busts! better luck next time...")
            print("Dealing again..")
            ourDealer.emptyHand()
            ourPlayer.emptyHand()
        if dealerSum > 21:
            print("Dealer busts! YOU WIN!")
            print("Dealing again..")
            ourDealer.emptyHand()
            ourPlayer.emptyHand()



main()
     





