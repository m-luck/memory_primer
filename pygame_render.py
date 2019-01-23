import request
import pygame
import sys
import random
import math
def launch_graphics(rows,cols,x=500,y=500):
    #initializes video
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 30)
    #sets the screen size
    screen = pygame.display.set_mode((x, y))
    paused = False
    blue=(0,0,255)
    red=(255,0,0)
    row_height = math.floor(y / rows)
    col_width = math.floor(x / cols)
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
    def renderText(text_string,x,y,w,h):
        new_text = font.render(text_string, True, (0xff, 0xff, 0xff))
        x = x - new_text.get_rect().width/2
        y = y - new_text.get_rect().height/2
        screen.blit(new_text,(x,y))
    def drawCards(row_height,col_width):
        text = "beebo"
        while (1):
            pause_state = eventHandler(paused)
            drawScreen()
            if paused is not True:
                drawCard(0,text,row_height,col_width,blue)
            else:
                drawCard(0,text,row_height,col_width,red)
            pygame.display.update()
    def drawCard(cueIndex,text,row_height,col_width,color):
        card_x = cueIndex * col_width
        card_y = cueIndex * row_height
        drawRect(color,card_x,card_y,col_width,row_height)
        renderText(text,card_x+col_width/2,card_y+row_height/2,col_width,row_height)
    drawCards(row_height,col_width)

launch_graphics(2,2)
