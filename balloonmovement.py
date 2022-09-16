import pygame
import sys
import time 
import random
from math import *
pygame.init()

screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Balloon Shooter Game")
clock = pygame.time.Clock()
direction=1
y=600
margin=100
lowerbound=100


    
while True:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    mouse_presses = pygame.mouse.get_pressed()
 
    if mouse_presses[0]:
        print("Left Mouse Key is being pressed")

    if mouse_presses[2]:
        print("right Mouse Key is being pressed")

    if mouse_presses[1]:
        print("middle Mouse Key is being pressed")


    	
    print(pygame.mouse.get_rel())
    
        # if event.type==pygame.mouse:
        #     position= pygame.mouse.get_pos()
        #     if position==pygame.mouse.get_pressed()
        #         pygame._del_pos()
                
    
    screen.fill((255,255,255))
    pygame.draw.circle(screen,(255,0,0),(750,y),20,0)
    pygame.draw.circle(screen,(255,0,0),(350,y),25,0)
    pygame.draw.circle(screen,(255,255,0),(40,y),20,0)
    pygame.draw.circle(screen,(0,250,0),(500,y),25,0)
    
    
    #pygame.display.update()
    clock.tick(60)
    if y==0:
        direction=1
    elif y==600:
        direction=-1
    y=y+direction
    
    pygame.display.update()