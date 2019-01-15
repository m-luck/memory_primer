import request
import pygame
import sys
import random

numberOfRows = 2
numberOfColumns = 3

top = 32
bottom = 42

#initializes video
pygame.init()

#sets the screen size
screen = pygame.display.set_mode((520, 350))
pause = False
blue=(0,0,255)
red=(255,0,0)


while (1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
    color = (255, 255, 255)
    screen.fill(color)
    #draws a rectangle on screen with color (r,g,b) at loc (x,y) of width w, height h.
    if pause != True:
        pygame.draw.rect(screen, blue,(200,150,100,50))
    else:
        pygame.draw.rect(screen, red,(200,150,100,50))

    pygame.display.update()
