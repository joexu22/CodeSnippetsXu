using System;
using System.Collections.Generic;

namespace InterviewExcersize{
    public class DeckProgram
    {
        enum Suit {
            Spades, Hearts, Diamonds, Clubs
        }
        
        enum Value {
            Ace, Two, Three, Four, Five, Six, Seven, Eight, Nine, Ten, Jack, Queen, King
        }

        class Card {
            /* cards are represented as a pair - a suit and a value */
            Suit suit { get; set; }
            Value value { get; set; }
            
            public Card(Suit s,  Value v)
            {
                suit = s;
                value = v;
            }
            
            public string getSuit()
            {
                return suit.ToString();
            }
            
            public string getValue()
            {
                return value.ToString();
            }
        }

        class Deck {
            /* a deck is represented as a list of cards */
            public List<Card> myDeck { get; set; }
            
            public Deck()
            {
                myDeck = new List<Card>();
                foreach (Suit s in Enum.GetValues(typeof(Suit)))
                {
                    foreach (Value v in Enum.GetValues(typeof(Value)))
                    {
                        myDeck.Add(new Card(s, v));
                    }
                }
            }
            
            /* individually move cards at random from one pile to another */
            public void ShuffleDeck()
            {
                List<Card> newDeck = new List<Card>();
                while (myDeck.Count > 0)
                {
                    Random random = new Random();
                    int randnum = random.Next(0, myDeck.Count);
                    newDeck.Add(myDeck[randnum]);
                    myDeck.RemoveAt(randnum);
                }
                myDeck.AddRange(newDeck);
            }
            
            /* view the suit and value of topmost card */
            public void DrawCard()
            {
                Card topcard = myDeck[0];
                Console.WriteLine(topcard.getValue() + " " + topcard.getSuit());
            }
        }

        static void Main(string[] args) {
            Deck deckofcards = new Deck();
            
            /* unshuffled deck */
            Console.WriteLine("First Card Should Be Ace of Spades:");
            deckofcards.DrawCard();
            
            Console.WriteLine();
            Console.WriteLine("The Rest Should Be Random (<Enter> to Shuffle, q to Quit): ");

            /* shuffles deck repeatly until exit */
            string exitFlag = "";
            do
            {
                deckofcards.ShuffleDeck();
                deckofcards.DrawCard();
                exitFlag = Console.ReadLine();
            }
            while(exitFlag != "q");
        }
    }
}