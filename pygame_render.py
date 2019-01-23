import pygame
import time
import sys
import random
import math
def launch_graphics(rows,cols,deck,w=500,h=500):
    #initializes video
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 30)
    #sets the screen size
    screen = pygame.display.set_mode((w, h))
    pause_state = False
    blue=(0,0,255)
    red=(255,0,0)
    row_height = math.floor(h / rows)
    col_width = math.floor(w / cols)
    def eventHandler(pause_state):
        reset = False
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pause_state = not pause_state
                    if event.key == pygame.K_r:
                        reset = True
        return pause_state, reset
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
    def drawCard(cueIndex,text,rows,cols,row_height,col_width,color):
        card_x = ((cueIndex%cols) * col_width)
        card_y = (math.floor(cueIndex/(rows+1)) * row_height)
        drawRect(color,card_x,card_y,col_width,row_height)
        renderText(text,card_x+col_width/2,card_y+row_height/2,col_width,row_height)
    def drawCardGrid(ind,deck,rows,cols,row_height,col_width,color):
        page = deck[ind]
        count = 0
        for cue in page:
            drawCard(count,cue,rows,cols,row_height,col_width,color)
            count += 1
    def drawCards(rows,cols,row_height,col_width,deck,pause_state):
        start = time.time()
        ind = 0
        while (1):
            time.sleep(0.1)
            pause_state, reset = eventHandler(pause_state)
            now = time.time()
            interval = 1.5
            if now - start > interval:
                start = time.time()
                if ind < len(deck)-1 and pause_state == False:
                    ind += 1
            if reset == True:
                reset = False
                if ind == len(deck)-1:
                    ind = 0
                    pause_state = False
            drawScreen()
            if pause_state is not True:
                drawCardGrid(ind,deck,rows,cols,row_height,col_width,blue)
            else:
                drawCardGrid(ind,deck,rows,cols,row_height,col_width,red)
            pygame.display.update()
    drawCards(rows,cols,row_height,col_width,deck,pause_state)
