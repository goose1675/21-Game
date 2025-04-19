import random



types = ["hearts", "diamonds", "spades", "clubs"]
num = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]

cards = []
for t in types:
    for n in num:
        cards.append(n + "of" + t) 

#This creates a deck of cards. The cards are lited as "ace of hearts", "2 of hearts", "3 of hearts"... and so on for 52 cards 
# Types stores the type of card, while num stores its number/value  


def add_card_points(card, to_dealer=True): # A function that when called, gives the player or dealer a score of points depending on the cards in their hand

    global dealer_point, playerpoint

    if "ace" in card:
        if to_dealer: 
            if dealer_point + 11 <= 21: #An if statement that decides if the ace should be counted as 10 point or 1 point, depending on the player or dealer's other cards. 
                points = 11 
            else:
                points = 1
        else:
            if playerpoint + 11 <= 21:
                points = 11
            else:
                points = 1
    
    elif "jack" in card or "queen" in card or "king" in card or "10" in card:
        points = 10
    else:
        points = int(card.split("of")[0])
    
    if to_dealer:
        dealer_point += points # If called to give a dealer points, to_dealer stays as a default: True
    else:
        playerpoint += points# If called to give the player points, to_dealer is False,

        
    
            

            

    





balance = 1000 #A set balance that every player starts with 
winnings = 0
running = True

while running: # The game loop 
    playerpoint = 0 # Variable for the total points the player recieves based off their cards
    dealer_point=0  # Variable for the total points the dealer recieves based off their cards 
    print("Your balance is at $", balance,  ".")
    bet = int(input("How much would you like to bet? "))
    while bet >= balance:
        print("You must bet less than or equal to your balance!") #Insures that the bet is not more than the balance
        bet = int(input("How much would you like to bet? "))

    balance = balance - bet
    print("Ok, you have placed your bet!") 


    
    playercard_1 = random.choice(cards) # The player's first card is pulled and then removed from the deck so it cant be pulled again by anyone else.
    cards.remove(playercard_1)
    
    dealercard_1 = random.choice(cards)# The dealer's first card is pulled and then removed from the deck so it cant be pulled again by anyone else.
    cards.remove(dealercard_1)
  

   
    print("The player's first card is ", playercard_1)
    add_card_points(playercard_1, to_dealer=False) #The players card is printed and a value is assigned
    print(playerpoint)


    print("The dealer's first card is ", dealercard_1)
    add_card_points(dealercard_1, to_dealer=True)  #The dealers card is printed and a value is assigned
    print(dealer_point)


    playercard_2 = random.choice(cards)
    cards.remove(playercard_2)
    
    print("The player's second card is ", playercard_2)
    add_card_points(playercard_2, to_dealer=False)
    print(playerpoint)

    if playerpoint == 21: #An auto win condition that shows that if the player hits 21, then they win 
        print("Auto win!")
        winnings = bet * 1.5
        print("You win ", winnings)
        balance += winnings
        print("Balance: ", balance)
        

    elif playerpoint < 21:
        choice = input("Would you like to hit (draw a new card) (h) or stand (keep your current hand) (s)? ").lower()
        while choice == "h":
            playercard_extra = random.choice(cards)
            cards.remove(playercard_extra)
            print("You draw: ", playercard_extra)
            add_card_points(playercard_extra, to_dealer=False)
            print("Player point total: ", playerpoint)
            if playerpoint >= 21:
                break
            choice = input("Hit again (h) or stand (s)? ").lower()

        

    dealercard_2 = random.choice(cards)
    cards.remove(dealercard_2)
    print("The dealer's second card is ", dealercard_2)
    add_card_points(dealercard_2, to_dealer=True)

    print(dealer_point)
    


    
    
    if dealer_point == 21:
        print("Dealer has Blackjack!")
        if playerpoint == 21:
            print("It's a tie!")
            balance += bet  # refund
        else:
            print("Dealer wins.")
        
        continue
    

    
    while dealer_point <= 16 and playerpoint < 21:
        dealercard_extra = random.choice(cards)
        cards.remove(dealercard_extra)
        print("Dealer draws:", dealercard_extra)
        add_card_points(dealercard_extra, to_dealer=True)

        print("Dealer total:", dealer_point)


    if playerpoint > 21:
        print("Bust! Dealer wins.")
        break
    elif dealer_point > 21 and playerpoint <  21:
        print("Dealer busts! You win!")
        balance += bet * 2
    elif playerpoint > dealer_point:
        print("You win!")
        balance += bet * 2
    elif playerpoint < dealer_point:
        print("Dealer wins.")
    
    else:
        print("It's a tie!")
        balance += bet

    
 

    


    print("Your new balance is ", balance)
    again = input("Play another round? (y/n): ").lower()
    if again != "y":
        print("Ok your final balance is: ", balance)
        print("Thank you for playing")
        
        running = False
    



    
















    

