import math
from random import randint
import pygame as pg
from pygame import mixer as mx

""" INITIALISING PYGAME """
pg.init()

""" CREAITNG SCREEN """
screen = pg.display.set_mode((800, 600))

""" BACKGROUND MUSIC """
# mx.music.load('lofi_background.wav')
# mx.music.set_volume(0.8)
# mx.music.play(-1)

background_music = mx.Sound("lofi_background.wav")
background_music.set_volume(0.8)
background_music.play()

""" TITLE """
pg.display.set_caption("ChristmasGame")

""" CREATING BACKGROUND IMAGE """
background = pg.image.load('bg.jpg')


""" CREATING PLAYER """
playerImg = pg.image.load("player.png")
playerX = 52
playerY = 5
playerX_change = 0
playerY_change = 0

""" CREATING CANDY """
candy = pg.image.load("candy.png")
candyX = randint(0,750)
candyY = randint(0,550)

score = 0

font = pg.font.Font("freesansbold.ttf",32)
over_text = pg.font.Font("freesansbold.ttf",64)
time_left = pg.font.Font("freesansbold.ttf",32)

""" SHOWING SCORE """
def show_score():
    score_text = font.render(f"Score : {score}",True, (255,255,255))
    screen.blit(score_text,(10,10))


""" SHOWING DEATH SCREEN """
def show_death(score):
    won = score>=15
    # if not done:win_music()
    text = "You Won!" if won else "You lose"
    over_text = font.render(text, True, (255,255,255))
    screen.blit(over_text, (300,300))
    


""" UPDATING THE PLAYER POSITION """
def player(x, y):
    screen.blit(playerImg,(x, y))

ticks = pg.time.get_ticks()

player_alive = True
""" GAME LOOP """
running = True
while running:
    screen.fill((0, 0, 0)) #FILLING BACKGROUND WITH BLACK, CHANGING THIS SPOILS EVERYTHING
    screen.blit(background,((0,0)))    
    screen.blit(candy, (candyX,candyY))

    """ COLLISION """
    if math.sqrt((candyX-playerX)**2+(candyY-playerY)**2)<=40:
        candyX=randint(0,750)
        candyY=randint(0,550)
        score += 1
        # print(score)

    """ O(n^2) stuff """
    for event in pg.event.get():
        if player_alive or event.type == pg.QUIT:
            if event.type == pg.KEYDOWN: 
                if event.key == pg.K_SPACE:
                    playerY_change=-0.4

                if event.key == pg.K_LEFT:
                    playerX_change = -0.5

                if event.key == pg.K_RIGHT:
                    playerX_change = 0.5

            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                    playerX_change = 0

            """ QUITTING GAME ON EXIT BUTTON """
            if event.type == pg.QUIT:running = False

    """ FAKE GRAVITY """
    playerY_change+=0.0009
    playerY+=playerY_change
    if playerY>=540:playerY=540
    if playerY<=5:playerY=5

    """ MOVING LEFT OR RIGHT """
    playerX+=playerX_change
    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736

    show_score()
    """ CHANGING POSITION OF PLYER"""
    player(playerX, playerY)                    

    seconds = (pg.time.get_ticks()-ticks)/1000
    if seconds>20:
        player_alive = False
        show_death(score)

    pg.display.update()
