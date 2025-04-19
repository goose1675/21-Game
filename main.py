import pygame
import sys 

from pygame.locals import * 
pygame.init() 




pygame.display.set_caption('Blackjack!')

     
WINDOW_SIZE = (1000,600) # set up window size base = 600, 400

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate screen

display = pygame.Surface((500, 300))


test_card_image = pygame.image.load("aceofhearts.png")
test_card_image = pygame.transform.scale(test_card_image, (150, 220))


card_rect = test_card_image.get_rect()
card_rect.topright = (WINDOW_SIZE[0] - 10, 10)  

running = True
while running:        
    screen.fill((144, 238, 144))
    screen.blit(test_card_image, card_rect)

    
    for event in pygame.event.get(): # event loop
        if event.type == QUIT: # check for window quit
            pygame.quit() # stop pygame
            sys.exit() # stop script

    pygame.display.update()
        

