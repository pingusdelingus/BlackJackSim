
from prettyprintcards import *


myDeck = Deck()
usrInput = input("what do you want to do: (D)eal | (Q)uit")
while (len(myDeck.d) != 0 and usrInput.upper() != 'Q'):
    usrInput = input("what do you want to do: (D)eal | (Q)uit")
    print(myDeck.deal_random())
    print(myDeck.prettyprint())

