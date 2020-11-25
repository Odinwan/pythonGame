import pygame
from assets.constants import *
from actions.touchAction import *

def move(player,touch):
    keys = pygame.key.get_pressed()
    if player.number == 1:
        a = {'left' : keys[pygame.K_a],
            'right' : keys[pygame.K_d],
            'jump' : keys[pygame.K_LSHIFT]}
    else:
        a = {'left' : keys[pygame.K_LEFT],
            'right' : keys[pygame.K_RIGHT],
            'jump' : keys[pygame.K_SPACE]}
    

    if not(touch): 
        if a.get('left'):
            if  player.x + player.speed > 2:
                if not touch:
                    if not player.left:
                        player.speed = 0
                    player.speed -= 1
                    player.x += player.speed
                    player.left = True
                    player.right = False
            else:
                player.x = 2
        elif a.get('right'):
            if  player.x + player.speed < (width - player.width - 2):
                if not touch:
                    if not player.right:
                        player.speed = 0
                    player.speed += 1
                    player.x += player.speed
                    player.left = False
                    player.right = True
                else:
                    player.x = (width - player.width - 2)  
        else:
            player.left = False
            player.right = False
            player.speed = 0
        if not(player.jump):
            if a.get('jump'):
                player.jump = True
        else:
            if player.jumpCount < 15:
                player.jumpCount += 1
                player.y -= 1
            elif player.jumpCount >= 15 and player.jumpCount <= 29:
                player.jumpCount += 1
                player.y += 1
                print(player.jumpCount)
            elif player.jumpCount >= 30:
                player.jumpCount = 0
                player.jump = False

def checkBorder(player):
    if  player.x <= 2:
        player.x = 2
    if  (player.x >= (width - player.width - 2)):
        player.x = (width - player.width - 2)  