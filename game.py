import random

#hello

types = ["hearts", "diamonds", "spades", "clubs"]
num = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]

def create_deck(): # A function that creates a deck of cards with 52 cards in total. 
    deck = []
    for t in types:
        for n in num:
            deck.append(n + " of " + t) 
    return deck

#This creates a deck of cards. The cards are lited as "ace of hearts", "2 of hearts", "3 of hearts"... and so on for 52 cards 
# Types stores the type of card, while num stores its number/value  


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
    
    def add_card(self, card):
        self.hand.append(card)
        self.calculate_points(card)

    def calculate_points(self, card):
        if "ace" in card:
            if self.points + 11 <= 21:
                self.points += 11
            else:
                self.points += 1
        elif "jack" in card or "queen" in card or "king" in card or "10" in card:
            self.points += 10
        else:
            self.points += int(card.split("of")[0])

    def reset_hand(self):
        self.hand = []
        self.points = 0
        self.blackjack = False
    
    def __str__(self):
        return self.name +  "'s hand: " + str(self.hand) + "| Points: " +  str(self.points)
    



        
    
            

            

    




#game loop function
def blackjack():
    deck = create_deck() # The deck is created using the create_deck function
    random.shuffle(deck) # This shuffles the deck to make sure the cards are random
    
    num_players = int(input("How many players are playing? (1-3): "))
    players = [Player(input("Enter a name for player" + str(i +1) + ": ")) for i in range(num_players)]
    dealer = Player("Dealer", is_dealer=True) 
   
    running = True
    # This keeps tge game running until the player decides to quit.
    while running: # The game loop 
        if len(deck) < 15:
            new_deck = create_deck()
            random.shuffle(new_deck)



        for player in players:
            player.reset_hand()
        dealer.reset_hand()

        bets = {}
        for player in players: 
            print("\n" + str(player.name) + "'s balance: " + str(player.balance))
            while True:
                bet = int(input("\n" + str(player.name) + ", enter your bet: "))
                if bet <= player.balance:
                    break
                print("Bet must be less than or equal to your balance.")
            player.balance -= bet 
            bets[player.name] = bet # This stores the players name and their bet in bets = {}  

        for player in players:
            for i in range(2):
                player.add_card(deck.pop()) #pop removes the last card in the deck and adds it to the players hand      
            print(player) # This prints the players hand and their points
            # for example: "Player 1's hand: ['ace of hearts', '2 of hearts'] | Points: 13"

        if player.points == 21:
            player.blackjack = True
            winnings = int(bets[player.name] * 1.5)
            player.balance += bets[player.name] + winnings
            print("\n", player.name, " hits BLACKJACK! You win $", winnings, "!")
            print("Your new balance is: $", player.balance)


        for i in range(2): # twice for the dealer                                        
            dealer.add_card(deck.pop()) #removes the las t card in the deck and adds it to the dealers hand
        print("\nDealer's hand: " + str(dealer.hand[0]) + " and a hidden card\n") # This prints the dealers hand with one card hidden
        #for example: "Dealer's hand: ['ace of hearts', '2 of hearts'] and a hidden card"

        for player in players: #each playur gets to play their turn 
            
            if player.blackjack:
                continue  # Skip turn if player already has Blackjack

            
            while player.points < 21: # The player can keep hitting until they reach 21 or bust
                choice = input(str(player.name) + ", do you want to hit (h) or stand (s)? ").lower()
                if choice == "h":
                    card = deck.pop() # The player draws a card from the deck
                    print("You drew: " + card)
                    player.add_card(card)
                    print(player) # This prints the players hand and their points
                else:
                    break #This breaks the loop and ends the players turn


        print("\nDealer's turn:") # The dealer's turn starts here
        print(dealer) # This prints the dealers hand and their points       
        while dealer.points < 17: 
              card = deck.pop() # The dealer draws a card from the deck
              dealer.add_card(card) # The card is added to the dealers hand
              print("Dealer drew: " + card  + " | Points:" + str(dealer.points)) # This prints the dealers hand and their points


        print("\n ----Final Results----") # The final results are printed here
        for player in players: 
            print("\n" + str(player.name) + ":" + str(player.points) + "vs Dealer:" + str(dealer.points)) 
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


        again = input("\nPlay another round? (y/n): ").lower()
        if again != "y":
            print("Thank you for playing")
            running = False
    


# Start the game
blackjack()














    

