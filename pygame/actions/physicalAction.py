import pygame
from assets.constants import *
from actions.touchAction import *
from modules.players import *
import time

def physicalAction(player,touch,window,index,player2):
    keys = pygame.key.get_pressed()
    if index == 1:
        controlKeys = {'left' : keys[pygame.K_a],
            'right' : keys[pygame.K_d],
            'strike' : keys[pygame.K_g],
            'jump' : keys[pygame.K_LSHIFT]}
    else:
        controlKeys = {'left' : keys[pygame.K_LEFT],
            'right' : keys[pygame.K_RIGHT],
            'strike' : keys[pygame.K_m],
            'jump' : keys[pygame.K_SPACE]}
            
    if not(player.hit):
        if controlKeys.get('left'):
            left(player)
        elif controlKeys.get('right'):
            right(player)
        else:
            stay(player)
        if controlKeys.get('strike'):
            if not(player.jump):
                if player2.actionType != 'shock':
                    player.hit = True

        if not(player.jump):
            if controlKeys.get('jump'):
                player.jump = True
        else:
            jump(player)

def checkBorder(player):
    if  player.rect.x <= 2:
        player.rect.x = 2
    if  (player.rect.x >= (width - 52 - 2)):
        player.rect.x = (width - 52 - 2)

#Движение влево
def left(player):
    player.actionType = 'walk'
    player.left = True
    player.right = False
    if  player.rect.x + player.speed > 2:
        if not player.left:
            player.speed = 0
        if not(player.speed == -4):
            player.speed -= 1
        player.rect.x += player.speed
    else:
        player.x = 2

#Движение вправо
def right(player):
    player.actionType = 'walk'
    player.left = False
    player.right = True
    if  player.rect.x + player.speed < (width - 52 - 2):
        if not player.right:
            player.speed = 0
        if not(player.speed == 4):
            player.speed += 1
        player.rect.x += player.speed
    else:
        player.rect.x = (width - 52 - 2)



#обычное состояние
def stay(player):
    if player.actionType != 'shock':
        if not(player.hit):
            player.actionType = 'stay'
            player.left = False
            player.right = False
            player.speed = 0
        else:
            player.actionType = 'stay'


#прыжок
def jump(player):
    player.actionType = 'jump'
    if player.jumpCount < 25:
        player.jumpCount += 1
        player.rect.y -= 2
        if player.left:
            player.rect.x -= 1
        if player.right:
            player.rect.x += 1
    elif player.jumpCount >= 25 and player.jumpCount <= 50:
        player.jumpCount += 1
        if (player.rect.y != 480):
            player.rect.y += 2
        if player.left:
            player.rect.x -= 1
        if player.right:
            player.rect.x += 1
    elif player.jumpCount > 50:
        player.jumpCount = 0
        player.jump = False

#Удар
def hit(box, player,playerAttack):
    if playerAttack.hit:
        playerAttack.actionType = 'attack'
        if playerAttack.attackCount <= 18:
            playerAttack.attackCount += 1
            #ПРоверка на касание
            if checkTouch(box, player) == 1: 
                    while player.shockCount <= 1000:
                        print(player.shockCount)
                        player.actionType = 'shock'
                        box.rect.x = playerAttack.rect.x                        
                        player.shockCount +=1
                    player.shockCount = 0
                    player.actionType ='stay'
        else:
            playerAttack.attackCount = 0
            playerAttack.hit = False
   

def checkTouch(attackPlayer,defPlayer):
    return checkCollision(attackPlayer, defPlayer)

