
import random
from colorama import Fore, Style, init
from pc import Deck, Player  # Assuming Deck and Player classes are in pc.py

# Initialize colorama
init(autoreset=True)

# Globals
numLoss = 0
numWins = 0

# Blackjack functions
def evaluate_hand(player):
    """
    Evaluate a player's hand in Blackjack.
    Returns the total value of the hand, accounting for Aces.
    """
    hand = player.hand
    sum_values = 0
    ace_count = 0

    for card in hand:
        if card is None:
            print("Error: Hand contains a None card.")
            return 0
        if card.getBJValue() == 11:
            ace_count += 1
        else:
            sum_values += card.getBJValue()

    # Adjust Ace values
    while ace_count > 0:
        if sum_values + 11 <= 21:
            sum_values += 11
        else:
            sum_values += 1
        ace_count -= 1

    return sum_values


def show_hand_value(player):
    """
    Display the value of a player's hand.
    """
    value = evaluate_hand(player)
    cards = ", ".join(c.shortprint() for c in player.hand)
    print(f"{player.name} has a hand: {cards} with value {Fore.RED}{value}")


def deal_card(person, deck):
    """
    Deal a single card to a person from the deck.
    """
    person.hand.append(deck.deal())


def initial_deal(player, dealer, deck):
    """
    Deal two cards each to the player and dealer.
    """
    for _ in range(2):
        deal_card(player, deck)
        deal_card(dealer, deck)


def dealer_turn(dealer, deck):
    """
    Perform the dealer's turn according to Blackjack rules.
    """
    while (dealer_value := evaluate_hand(dealer)) < 17:
        deal_card(dealer, deck)
        show_hand_value(dealer)

    if dealer_value > 21:
        print(f"{Fore.RED}Dealer busts!{Style.RESET_ALL}")
    else:
        print(f"Dealer stands with {dealer_value}")


def compare_hands(dealer_sum, player_sum):
    """
    Compare dealer and player hands to determine the result.
    """
    if player_sum > 21:
        print(f"{Fore.RED}Player busts with {player_sum}{Style.RESET_ALL}")
    elif dealer_sum > 21:
        print(f"{Fore.GREEN}Player wins! Dealer busts with {dealer_sum}{Style.RESET_ALL}")
    elif dealer_sum > player_sum:
        print(f"{Fore.RED}Dealer wins with {dealer_sum} against player's {player_sum}{Style.RESET_ALL}")
    elif dealer_sum < player_sum:
        print(f"{Fore.GREEN}Player wins with {player_sum} against dealer's {dealer_sum}{Style.RESET_ALL}")
    else:
        print(f"Tie: Both have {player_sum}")

deck = Deck()
deck.start()
def blackjack():
    """
    Main Blackjack gameplay loop.
    """

    human = Player('Human')
    dealer = Player('Dealer')
    initial_deal(human, dealer, deck)

    show_hand_value(human)
    player_sum = evaluate_hand(human)
    dealer_sum = evaluate_hand(dealer)

    while player_sum <= 21:
        print(f"The dealer is showing a {dealer.hand[0]}")
        action = input("What would you like to do? (H)it | (S)tand | (K)Surrender | e(X)it: ").strip().lower()

        if action == 'h':  # Hit
            deal_card(human, deck)
            show_hand_value(human)
            player_sum = evaluate_hand(human)
        elif action == 's':  # Stand
            dealer_turn(dealer, deck)
            dealer_sum = evaluate_hand(dealer)
            compare_hands(dealer_sum, player_sum)
            break
        elif action == 'k':  # Surrender
            print("You surrendered the hand.")
            return
        elif action == 'x':  # Exit
            print("Goodbye!")
            exit()
        else:
            print("Invalid input. Please choose again.")

    if player_sum > 21:
        print(f"{Fore.RED}Player busts with {player_sum}{Style.RESET_ALL}")


def main():
    """
    Main function to play multiple games of Blackjack.
    """
    while not deck.isEmpty():
        blackjack()
        replay = input("Would you like to play again? (Y/N): ").strip().upper()
        if replay != 'Y':
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
