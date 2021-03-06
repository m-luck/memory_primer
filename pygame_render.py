# Written in 2017 -- Not representative
import pygame
import time
import sys
import random
import math
to_learn = []
rects = {}
def launch_graphics(rows,cols,deck,w=500,h=500):
    #initializes video
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont('liberationserif', 25)
    #sets the screen size
    screen = pygame.display.set_mode((w, h))
    pause_state = False
    blue=(255,147,55)
    red=(255,80,43)
    row_height = math.floor(h / rows)
    col_width = math.floor(w / cols)
    phrase_clicks = {}
    def eventHandler(pause_state, old_pause):
        global to_learn
        reset = False
        finished = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mpos = pygame.mouse.get_pos()
                for rect in rects:
                    if rects[rect][0].collidepoint(mpos):
                        print(rects[rect])
                        text = rects[rect][1]
                        url = text.split(' ')
                        url = '+'.join(url)
                        url = str("https://google.com/search?q="+url)
                        print(url)
                        to_learn.append(url)
                        if text in phrase_clicks:
                            phrase_clicks[text] += 1
                        else:
                            phrase_clicks[text] = 0
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause_state = not pause_state
                if event.key == pygame.K_r:
                    reset = True
                    pause_state = False
                if event.key == pygame.K_q:
                    finished = True
        return pause_state, reset, old_pause, finished
    def drawScreen():
        color = (230, 230, 230)
        screen.fill(color)
    def drawRect(color, x, y, w, h, text): # includes open url function
        new_rect = pygame.draw.rect(screen, color, (x,y,w,h))
        global rects
        rects[str(new_rect)] = (new_rect,text)
        return new_rect
    def renderText(text_string,x,y,w,h):
        new_text = font.render(text_string, True, (0xff, 0xff, 0xff))
        x = x - new_text.get_rect().width/2
        y = y - new_text.get_rect().height/2
        screen.blit(new_text,(x,y))
    def drawCard(cueIndex,text,rows,cols,row_height,col_width,color):
        card_x = ((cueIndex%cols) * col_width)
        card_y = (math.floor(cueIndex/cols) * row_height)
        drawRect(color,card_x,card_y,col_width,row_height,text)
        renderText(text,card_x+col_width/2,card_y+row_height/2,col_width,row_height)
    def drawCardGrid(ind,deck,rows,cols,row_height,col_width,color):
        page = deck[ind]
        count = 0
        for cue in page:
            drawCard(count,cue,rows,cols,row_height,col_width,color)
            count += 1
    def init_stats(deck):
        cue_stats = {}
        for page in deck:
            for cue in page:
                cue_stats[cue] = []
        return cue_stats
    def update_stats(ind,deck,pause_length,cue_stats):
        page = deck[ind]
        for cue in page:
            cue_stats[cue].append(pause_length,)
        return cue_stats
    def drawCards(rows,cols,row_height,col_width,deck,pause_state):
        response_times = []
        start = time.time()
        ind = 0
        pause_end = time.time()
        pause_start = 0
        pause_end = 0
        old_pause = False
        cue_stats = init_stats(deck)
        finished = False
        screen_start = time.time()
        while (finished == False):
            time.sleep(0.1)
            pause_state, reset, old_pause, finished = eventHandler(pause_state, old_pause)
            now = time.time()
            interval = 2.0
            if now - start > interval:
                start = time.time()
                if ind < len(deck)-1 and pause_state == False:
                    rects = {}
                    ind += 1
                    screen_start = time.time()
            if reset == True:
                reset = False
                if ind == len(deck)-1:
                    ind = 0
                    pause_state = False
            drawScreen()
            if pause_state is not True:
                drawCardGrid(ind,deck,rows,cols,row_height,col_width,blue)
                if old_pause is True:
                    pause_end = time.time()
                    old_pause = False
                    cue_stats = update_stats(ind,deck,pause_end-pause_start,cue_stats)
            else:
                drawCardGrid(ind,deck,rows,cols,row_height,col_width,red)
                if old_pause is False:
                    pause_start = time.time()
                    old_pause = True
                    screen_pause = time.time()
                    response_times.append(screen_pause-screen_start)
            pygame.display.update()
        file = open("response_times.txt","a+")
        string = "\n"+str(time.time()) +":"+str(response_times)
        file.write(string)
        file.close()
        file = open("avg_click.txt","a+")
        string = str(time.time()) + ":" + str(phrase_clicks)
        file.write(string)
        file.close()
        file = open("to_learn_from_recent_session.txt", "w+")
        file.write(str(to_learn))
        file.close()
        return cue_stats
    cue_stats = drawCards(rows,cols,row_height,col_width,deck,pause_state)

    return cue_stats, time.time()
