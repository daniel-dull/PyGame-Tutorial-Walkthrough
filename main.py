"""
This repository is intended as practice and follows along with a YouTube tutorial.

Tutorial Link: https://www.youtube.com/watch?v=AY9MnQ4x3zk


"""
import pygame
import sys

pygame.init() #initializes all of python
screen = pygame.display.set_mode((800,400)) #creates display surface. 
pygame.display.set_caption('Runner') # gives the window a title, supposedly. 
clock = pygame.time.Clock() # helps with tracking frame rate and time. 
test_font = pygame.font.Font('UltimatePygameIntro-main/font/Pixeltype.ttf',50)

sky = pygame.image.load('UltimatePygameIntro-main/graphics/Sky.png')
ground = pygame.image.load('UltimatePygameIntro-main/graphics/ground.png')
text_surface = test_font.render('My Game', False, 'Black')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    screen.blit(sky,(0,0)) 
    screen.blit(ground,(0,300))
    screen.blit(text_surface,(300,50))

    pygame.display.update()
    clock.tick(60)





































