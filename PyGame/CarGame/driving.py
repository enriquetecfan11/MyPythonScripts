import pygame
from pygame.locals import *
import time
import math
 
pygame.init()
track = pygame.image.load("resources/images/track.png")
player = pygame.image.load("resources/images/car.png")

screen = pygame.display.set_mode((900,500))


trackx= -3555.181577
tracky = -1684.63965

xpos = 450
ypos = 350


keys=[False,False,False,False]
direction = 0
forward = 0


running = 1
while running:
    pygame.display.set_caption('driving')
    screen.fill(0)
 
    if keys[0]==True:
        direction+= 2
    if keys[1]==True:
        direction-= 2
    if keys[2]==True:
        forward-= 0.2
    if keys[3]==True and forward <= 0:
        forward+= 0.2
     
    movex=math.cos(direction/57.29)*forward
    movey=math.sin(direction/57.29)*forward
    
    trackx+=movex
    tracky-=movey
 
    playerrot = pygame.transform.rotate(player,direction)
    screen.blit(track, (trackx,tracky))
    screen.blit(playerrot, (xpos,ypos))
    pygame.display.flip()
     
    time.sleep(0.02)
 
    for event in pygame.event.get():
    # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
 
        if event.type == pygame.KEYDOWN:
            if event.key==K_LEFT:
                keys[0]=True
            elif event.key==K_RIGHT:
                keys[1]=True
            elif event.key==K_UP:
                keys[2]=True
            elif event.key==K_DOWN:
                keys[3]=True
            elif event.key==pygame.K_ESCAPE:
                pygame.quit()
 
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                keys[0]=False
            elif event.key==pygame.K_RIGHT:
                keys[1]=False
            elif event.key==pygame.K_UP:
                keys[2]=False
            elif event.key==pygame.K_DOWN:
                keys[3]=False
            elif event.key==pygame.K_ESCAPE:
                pygame.quit()


    if (trackx >= -2077.63 ):
        print("Empieza el tiempo")
    
    print("Player Pos.Y: " + str(trackx))
    print("Player Pos.X: " + str(tracky))
                
pygame.quit()