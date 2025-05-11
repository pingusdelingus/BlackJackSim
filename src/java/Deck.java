import java.util.Random;

public class Deck {

  PlayingCard[] thedeck;
  int deckIndex;
  float numberOfCardsIn;
  float deckPenetration; // how long until deck is shuffled ** VERY IMPORTANT for variance calculations
  // high deck penetration (means more cards dealt until shuffle) better odds, low penetration(cards shuffled more often) --> bad odds
 float MAX_CARDS_IN_DECK = 52.0f;

// debug main
  public static void main(String[] args) {
    
    Deck myDeck = new Deck(0.65f);

    System.out.println(myDeck);
    
  }// end of main
  //
  public String toString(){
    StringBuilder str = new StringBuilder();
    for (int index = this.deckIndex; index < this.thedeck.length; index++){
      str.append(this.thedeck[index]);
      str.append(" | ");
    }
    return str.toString();
  }// end of toString
  
  

  public Deck(float inputDeckPen)
  {
    System.out.println("inside constructor");
  this.deckPenetration = inputDeckPen;
    thedeck = new PlayingCard[52];
    numberOfCardsIn = 52.0f;
    int deckIndex = 0;
    System.out.println("calling shuffle in constructor");
    shuffle();
  }// end of deck constructor


  // deal one card from the deck and return to caller
  public PlayingCard Deal()
  {
  float percentageLeft = this.numberOfCardsIn / MAX_CARDS_IN_DECK;


    if (percentageLeft > deckPenetration)
    {
     PlayingCard selectedCard = thedeck[deckIndex];
      deckIndex++;
      numberOfCardsIn = numberOfCardsIn - 1;
      return selectedCard;
    }
    else if (percentageLeft >= deckPenetration)
   {
      System.out.println("Reached Penetration Limit, reshuffling");
      shuffle();
     PlayingCard selectedCard = thedeck[deckIndex];
      deckIndex++;
      numberOfCardsIn = numberOfCardsIn - 1;
      return selectedCard;
    }
    System.err.println("wtf going on, check Deal method ");
    return null; // should only happen if error 

  }// end of deal method
 

  // shuffles the deck
  public void shuffle(){
    System.out.println("Setting all ptrs to null");
   for (int i = 0; i < this.thedeck.length; i++) { this.thedeck[i] = null;} // setting all pointers to null
    
    Suit[] suits = {Suit.Diamonds, Suit.Hearts, Suit.Clubs, Suit.Spades}; 
      System.out.println("initalizing all cards");

    //initialize all cards in the deck
    for(int suitIndex = 1; suitIndex <=4; suitIndex++){
      for (int numIndex = 1; numIndex <= 13; numIndex++){
                
          PlayingCard current = new PlayingCard(suits[suitIndex - 1], numIndex);
          this.thedeck[(suitIndex -1) + (numIndex - 1)] = current; 
      }// end of inner
     
      
    }// end of outer
  

    for(int i = 0; i < this.thedeck.length; i++){System.out.println(this.thedeck[i] + " | ");}
    // need to shuffle deck now

    int shuffleIndex = 0;

    while (shuffleIndex < 2)
  {
   shuffleArray(this.thedeck); 
      shuffleIndex++;
  }// end of whlie loop
  

  }// end of shulffe method


public void shuffleArray(PlayingCard[] array) {
    Random rnd = new Random();
    for (int i = array.length - 1; i > 0; i--) {
        int index = rnd.nextInt(i + 1);
        // Simple swap
        PlayingCard temp = array[index];
        array[index] = array[i];
        array[i] = temp;
    }
}// end of shuffleArray method

}// end of deck class
