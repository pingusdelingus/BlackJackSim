public class PlayingCard 
{

  public Suit cardSuit;

  public int cardNumber;

  public PlayingCard(Suit inputSuit, int inputNumber)
  {
    this.cardSuit = inputSuit;
    this.cardNumber = inputNumber;
  }// end of constructor

  public String toString()
  {
    String s1 = this.cardNumber + " of " +  this.cardSuit;
    return s1;
  }// end of to string



/*
  public static void main(String[] args) {
      PlayingCard c1 = new PlayingCard(Suit.Diamonds, 7);

      System.out.println(c1);


  }// end of main

*/  
}// end of class PlayingCard
