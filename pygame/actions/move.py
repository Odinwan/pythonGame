import pygame
from assets.constants import *
from actions.touchAction import *
from modules.players import *
import time

def actionPlayer(player,touch,window,index):
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
def hit(player):
    player.actionType = 'attack'
    if player.attackCount <= 18:
        player.attackCount += 1
    else:
        player.attackCount = 0
        player.hit = False

def checkAttack(player):
    if player.hit: hit(player)


# def hit(player1,player2,lifeBox1, lifeBox2):
#         if player1.hit:
#             player1.actionType = 'attack'
#             player1.animCount += 1
#             if (player1.animCount < 15):
#                 if player1.position == 'right':
#                     player1.rect.width += 5
#                 elif player1.position == 'left':
#                     player1.rect.width -= 5
#                 if (checkTouch(player1,player2) == 1):
#                     if player1.rect.x > player2.rect.x:
#                         player1.rect.x += 5
#                         player2.rect.x -= 10
#                     else:
#                         player1.rect.x -= 5
#                         player2.rect.x += 10
#                     if player1.animCount == 14:
#                         CheckLife(lifeBox2,player2.number,15)
#             elif (15 <= player1.animCount <= 45):
#                 player1.rect.width -= 5
#                 if (player1.rect.width <= 52):
#                     player1.rect.width = 52
#                     player1.actionType = 'stay'
#                     player1.hit = False
#                     player1.animCount = 0
#         elif(player2.hit):
#             player2.animCount += 1
#             if (player2.animCount < 15):
#                 player2.rect.width += 5
#                 if (checkTouch(player2,player1) == 1):
#                     print('attack')
#             elif (15 <= player2.animCount <= 30):
#                 player2.rect.width -= 5
#                 if (player2.rect.width <= 52):
#                     player2.rect.width = 52
#                     player2.hit = False
#                     player2.animCount = 0

def checkTouch(attackPlayer,defPlayer):
    return checkCollision(attackPlayer, defPlayer)
