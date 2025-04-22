import random


"""from player_class import Player # This imports the Player class from the player_class file""" #not needed anymore


class Player:# My first class that stores the player and dealer's information.
    def __init__(self, name, is_dealer=False): 
        self.name = name
        self.hand = [] # The hand is a list that stores the cards the player has in their hand.
        self.points = 0
        self.is_dealer = is_dealer #A way to check if the player is a dealer 
        self.blackjack = False # A way to check if the player has a blackjack
        if is_dealer!= True: 
            self.balance = 1000
        else:
            self.balance = 0
    
    def add_card(self, card): # This adds a card to the player's hand and calculates the points
        self.hand.append(card)
        self.calculate_points(card)

    def calculate_points(self, card):# This calculates the points for the player based on the card they have drawn
        if "ace" in card:
            if self.points + 11 <= 21:
                self.points += 11
            else:
                self.points += 1
        elif "jack" in card or "queen" in card or "king" in card or "10" in card: 
            self.points += 10
        else:
            self.points += int(card.split("of")[0]) # This splits the card string and gets the number of the card 

    def reset_hand(self): # This resets the player's hand and points for the next round
        self.hand = []
        self.points = 0
        self.blackjack = False
    
    def take_turn(self, deck):
        if self.blackjack:
            return  # Skip turn if player already has Blackjack

        while self.points < 21: # This loop asks the player if they want to hit or stand
            choice = input("\n" + self.name + ", would you like to Hit(h) or Stand(s)? ").lower()
            if choice == "h":
                card = deck.pop()
                print("You drew:", card)
                self.add_card(card)# This adds the card to the player's hand and calculates the points
                print(self)
            else:
                break
    
    def __str__(self): # This prints the player's hand and points
        return self.name +  "'s hand: " + str(self.hand) + "| Points: " +  str(self.points)
    




types = ["hearts", "diamonds", "spades", "clubs"]
num = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
# This creates a list of types and numbers for the cards

def create_deck(): # A function that creates a deck of cards with 52 cards in total. 
    deck = []
    for t in types:
        for n in num:
            deck.append(n + " of " + t) 
    return deck

#This creates a deck of cards. The cards are lited as "ace of hearts", "2 of hearts", "3 of hearts"... and so on for 52 cards 
# Types stores the type of card, while num stores its number/value  
     


#game loop function
def blackjack():
    deck = create_deck() # The deck is created using the create_deck function
    random.shuffle(deck) # This shuffles the deck to make sure the cards are random
    print("\n ----🃏 Welcome to 21! 🃏----")
    num_players = int(input("How many players are playing? (1-3): "))
    players = [Player(input("Enter a name for player " + str(i +1) + ": ")) for i in range(num_players)]
    dealer = Player("Dealer", is_dealer=True) 
   


   
    running = True
    # This keeps tge game running until the player decides to quit.
    
    while running: 
        
        if len(deck) < 15:   
            new_deck = create_deck()
            random.shuffle(new_deck)
        # This checks if the deck has less than 15 cards left. If it does, a new deck is created and shuffled.


        for player in players:
            player.reset_hand()
        dealer.reset_hand()
        # This resets the players and dealers hands 

        bets = {}
        for player in players: 
            print("\n" + str(player.name) + "'s balance: " + str(player.balance))
            while True:
                print("--------------------")
                bet = int(input("\n" + str(player.name) + ", enter your bet: "))
               
                if bet <= player.balance:
                    break
                print("Bet must be less than or equal to your balance.")
                
            player.balance -= bet 
            bets[player.name] = bet # This stores the players name and their bet in bets = {}  


        # This loop prints the players bets
        #It subtracts the bet from the players balance and stores it in the bets dictionary
        #If the bet is more than the players balance, it prints an error message and asks for a new bet




    
        print("----------Dealing Cards---------")
        for player in players:
            for i in range(2):
                player.add_card(deck.pop()) #pop removes the last card in the deck and adds it to the players hand      
            print(player)
            print("\n") #
            # This prints the players hand and their points
            # for example: "Player 1's hand: ['ace of hearts', '2 of hearts'] | Points: 13"



        if player.points == 21:
            player.blackjack = True
            winnings = int(bets[player.name] * 1.5)
            player.balance += bets[player.name] + winnings
            print("\n🎉", player.name, " hits BLACKJACK! You win $", winnings, "!")
            print("Your new balance is: $", player.balance)
        # This checks if the player has a blackjack. If they do, they win 1.5 times their bet 



        for i in range(2): # twice for the dealer                                        
            dealer.add_card(deck.pop()) #This removes the las t card in the deck and adds it to the dealers hand
        print("\nDealer's hand: " + str(dealer.hand[0]) + " and a hidden card\n") # This prints the dealers hand with one card hidden
        #for example: "Dealer's hand: ['ace of hearts', '2 of hearts'] and a hidden card"

         #each playur gets to play their turn 
        for player in players:
            player.take_turn(deck)    
      # Skip turn if player already has Blackjack

       
        print("\nDealer's turn:") # The dealer's turn starts here
        print(dealer) # This prints the dealers hand and their points       
        while dealer.points < 17: 
              card = deck.pop() # The dealer draws a card from the deck
              dealer.add_card(card) # The card is added to the dealers hand
              print("Dealer drew: " + card  + " | Points: " + str(dealer.points)) # This prints the dealers hand and their points



        print("\n ----Final Results----") # The final results are printed here
        for player in players: 
            print("\n" + str(player.name) + ": " + str(player.points) + " vs Dealer: " + str(dealer.points)) 
            # This prints the players hand and their points vs the dealers hand and their points
            # for example: "Player 1: 13 vs Dealer: 17"

            if player.points > 21: # If the player busts, they lose
                print(player.name + " busts! Dealer wins.")
                print("Your new balance is: " + str(player.balance))

            elif dealer.points > 21 or player.points > dealer.points: 
            # If the dealer busts or the player has a higher score, the player wins 
                winnings = bets[player.name] * 2
                player.balance += winnings
                print(player.name + " wins! You win $" + str(winnings) + ".")
                print("Your new balance is: " + str(player.balance))
            elif player.points == dealer.points:
                player.balance += bets[player.name]
                print(player.name + " ties with the dealer. Your bet is returned.")    
            else: # If the dealer has a higher score, the dealer wins
                print(player.name + " loses. Dealer wins.")
                print("Your new balance is: " + str(player.balance))
            # This prints the players balance after the game


        again = input("\nPlay another round? (y/n): ").lower()
        if again != "y":
            print("--------------------")
            print("\n\n🎉 Thank you for playing! 🎉\n")
            print("--------------------")
            running = False
        # This checks if the player wants to play again. 
        # If they do, the game restarts. If they don't, the game ends
        #  
    


# Start the game
blackjack()
#Call the blackjack function


