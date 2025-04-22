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
    
    def take_turn(self, deck):
        if self.blackjack:
            return  # Skip turn if player already has Blackjack

        while self.points < 21:
            choice = input("\n" + self.name + ", would you like to Hit(h) or Stand(s)? ").lower()
            if choice == "h":
                card = deck.pop()
                print("You drew:", card)
                self.add_card(card)
                print(self)
            else:
                break
    
    def __str__(self):
        return self.name +  "'s hand: " + str(self.hand) + "| Points: " +  str(self.points)
    