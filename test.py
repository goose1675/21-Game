import random
from player_class import Player
import pygame
import sys
from pygame.locals import *
from assets import *  # This imports the assets from the assets file

# Initialize Pygame
pygame.init()

# Set up the game window
pygame.display.set_caption('Blackjack!')
WINDOW_SIZE = (1000, 600)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

# Set up basic colors and fonts
GREEN = (0, 128, 0)
WHITE = (255, 255, 255)
font = pygame.font.SysFont('Arial', 20)

# Game logic to create a deck of cards
types = ["hearts", "diamonds", "spades", "clubs"]
num = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]

def create_deck():
    deck = []
    for t in types:
        for n in num:
            deck.append(n + " of " + t)
    random.shuffle(deck)
    return deck

# Load card images (ensure you have a folder "assets" with the respective images)
def load_card_images():
    images = {}
    for t in types:
        for n in num:
            card_name = f"{n}of{t}.png"
            try:
                images[f"{n} of {t}"] = pygame.image.load(f"assets/{card_name}")
            except pygame.error:
                images[f"{n} of {t}"] = pygame.Surface((100, 150))
                images[f"{n} of {t}"].fill(WHITE)
    return images

# Game loop function
def blackjack():
    # Set up the deck and the images
    deck = create_deck()
    images = load_card_images()
    
    # Create player and dealer
    player = Player("Player 1")
    dealer = Player("Dealer", is_dealer=True)
    
    # Deal cards to player and dealer
    player.add_card(deck.pop())
    player.add_card(deck.pop())
    dealer.add_card(deck.pop())
    dealer.add_card(deck.pop())

    # Game loop
    running = True
    while running:
        screen.fill(GREEN)
        
        # Display player and dealer hands
        display_player_hand(player, 50, 400, images)
        display_dealer_hand(dealer, 50, 50, images)
        
        # Display points
        display_text(f"{player.name}'s Points: {player.points}", 50, 550)
        display_text(f"Dealer's Points: {dealer.points}", 50, 20)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_h:  # Player chooses to hit
                    player.add_card(deck.pop())
                elif event.key == K_s:  # Player chooses to stand
                    dealer_turn(dealer, deck, images)
                    running = False
        
        pygame.display.update()

def display_player_hand(player, x, y, images):
    """Displays the player's hand on the screen."""
    for i, card in enumerate(player.hand):
        screen.blit(images[card], (x + i * 120, y))

def display_dealer_hand(dealer, x, y, images):
    """Displays the dealer's hand on the screen, hiding the second card."""
    for i, card in enumerate(dealer.hand):
        if i == 1 and not dealer.is_dealer:
            pygame.draw.rect(screen, WHITE, (x + i * 120, y, 100, 150))
        else:
            screen.blit(images[card], (x + i * 120, y))

def display_text(text, x, y):
    """Displays text on the screen."""
    label = font.render(text, True, WHITE)
    screen.blit(label, (x, y))

def dealer_turn(dealer, deck, images):
    """Handle the dealer's turn."""
    while dealer.points < 17:
        dealer.add_card(deck.pop())
        pygame.time.delay(1000)  # Delay to simulate drawing cards
        screen.fill(GREEN)
        display_dealer_hand(dealer, 50, 50, images)
        display_player_hand(dealer, 50, 400, images)
        display_text(f"{dealer.name}'s Points: {dealer.points}", 50, 20)
        pygame.display.update()

# Start the game
blackjack()
