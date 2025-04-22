import random
from player_class import Player # This imports the Player class from the player_class file
import pygame
import sys 
from pygame.locals import * 

from assets import * # This imports the assets from the assets file


pygame.init() 

pygame.display.set_caption('Blackjack!')

     
WINDOW_SIZE = (1000,600) # set up window size base = 600, 400
screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate screen
display = pygame.Surface((500, 300))







#

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
            


def load_card_image(card_name):
    card_name = card_name.replace(" ", "")  # remove spaces
    card_name = card_name.lower()           # make lowercase
    path = f"assets/{card_name}.png"        # image path
    try:
        image = pygame.image.load(path)
        image = pygame.transform.scale(image, (100, 150))
        return image
    except:
        print(f"Image for '{card_name}' not found.")
        return None


def draw_hand(hand, x, y):
    for i, card in enumerate(hand):
        card_img = load_card_image(card)
        if card_img:
            screen.blit(card_img, (x + i * 110, y))  # adjust spacing



"""test_card_image = pygame.image.load("assets/" + "aceofhearts.png")
test_card_image = pygame.transform.scale(test_card_image, (150, 220))


card_rect = test_card_image.get_rect()
card_rect.topright = (WINDOW_SIZE[0] - 10, 10)  
"""


#game loop function
def blackjack():
    """deck = create_deck() # The deck is created using the create_deck function
    random.shuffle(deck) # This shuffles the deck to make sure the cards are random
    
    num_players = int(input("How many players are playing? (1-3): "))
    players = [Player(input("Enter a name for player " + str(i +1) + ": ")) for i in range(num_players)]
    dealer = Player("Dealer", is_dealer=True) 
   """
    running = True
    # This keeps tge game running until the player decides to quit.
    
    while running: 
        screen.fill((144, 238, 144))
        sample_player_hand = ["ace of hearts", "7 of clubs"]
        sample_dealer_hand = ["queen of diamonds", "5 of spades"]

        draw_hand(sample_player_hand, 50, 400)  # Draw player cards near bottom
        draw_hand(sample_dealer_hand, 50, 100)  # Draw dealer cards near top


    
        for event in pygame.event.get(): # event loop
            if event.type == QUIT: # check for window quit
                pygame.quit() # stop pygame
                sys.exit() # stop script

        pygame.display.update()
        


    




        """if len(deck) < 15:
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


        again = input("\nPlay another round? (y/n): ").lower()
        if again != "y":
            print("Thank you for playing")
            running = False
    
"""

# Start the game
blackjack()














    

