import request
import pygame
import sys
import random
def launch_graphics(cues,pages):
    #initializes video
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 30)
    #sets the screen size
    screen = pygame.display.set_mode((520, 350))
    paused = False
    blue=(0,0,255)
    red=(255,0,0)
    def eventHandler(pause_state):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pause_state = not pause_state
        return pause_state
    def drawScreen():
        color = (230, 230, 230)
        screen.fill(color)
    def drawRect(color, x, y, w, h):
        new_rect = pygame.draw.rect(screen, color, (x,y,w,h))
        return new_rect
    def renderText(text_string):
        new_text = font.render(text_string, True, (0xff, 0xff, 0xff))
        screen.blit(new_text,(200,150))
    def drawCard(cueIndex):
        while (1):
            paused = eventHandler(paused)
            drawScreen()
            if paused is not True:
                drawRect(blue)
                renderText("beebo")
            else:
                drawRect(red)
                renderText("beebo ")
            pygame.display.update()
    drawCard()

launch_graphics(0,0)
