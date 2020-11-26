import pygame
from assets.constants import *
from actions.touchAction import *
from modules.players import *
import time

def move(player,touch):
    keys = pygame.key.get_pressed()
    if player.number == 1:
        a = {'left' : keys[pygame.K_a],
            'right' : keys[pygame.K_d],
            'strike' : keys[pygame.K_g],
            'jump' : keys[pygame.K_LSHIFT]}
    else:
        a = {'left' : keys[pygame.K_LEFT],
            'right' : keys[pygame.K_RIGHT],
            'strike' : keys[pygame.K_m],
            'jump' : keys[pygame.K_SPACE]}

    if a.get('left'):
        if  player.rect.x + player.speed > 2:
            if not touch:
                if not player.left:
                    player.speed = 0
                player.speed -= 1
                player.rect.x += player.speed
                player.left = True
                player.right = False
        else:
            player.x = 2
    elif a.get('right'):
        if  player.rect.x + player.speed < (width - 52 - 2):
            if not touch:
                if not player.right:
                    player.speed = 0
                player.speed += 1
                player.rect.x += player.speed
                player.left = False
                player.right = True
            else:
                player.rect.x = (width - 52 - 2)
    else:
        player.left = False
        player.right = False
        player.speed = 0
    if a.get('strike'):
        if not(player.hit):
            player.hit = True
    if not(player.jump):
        if a.get('jump'):
            player.jump = True
    else:
        if player.jumpCount < 15:
            player.jumpCount += 1
            player.rect.y -= 1
        elif player.jumpCount >= 15 and player.jumpCount <= 29:
            player.jumpCount += 1
            player.rect.y += 1
            print(player.jumpCount)
        elif player.jumpCount >= 30:
            player.jumpCount = 0
            player.jump = False

def checkBorder(player):
    if  player.rect.x <= 2:
        player.rect.x = 2
    if  (player.rect.x >= (width - 52 - 2)):
        player.rect.x = (width - 52 - 2)

def hit(player1,player2,lifeBox1, lifeBox2):
        if player1.hit:
            player1.animHit += 1
            if (player1.animHit < 15):
                player1.rect.width += 5
                if (checkTouch(player1,player2) == 1):
                    if player1.rect.x > player2.rect.x:
                        player1.rect.x += 5
                        player2.rect.x -= 10
                    else:
                        player1.rect.x -= 5
                        player2.rect.x += 10
                    if player1.animHit == 14:
                        CheckLife(lifeBox2,player2.number,15)


            elif (15 <= player1.animHit <= 30):
                player1.rect.width -= 5
                if (player1.rect.width <= 52):
                    player1.rect.width = 52
                    player1.hit = False
                    player1.animHit = 0
        elif(player2.hit):
            player2.animHit += 1
            if (player2.animHit < 15):
                player2.rect.width += 5
                if (checkTouch(player2,player1) == 1):
                    print('attack')
            elif (15 <= player2.animHit <= 30):
                player2.rect.width -= 5
                if (player2.rect.width <= 52):
                    player2.rect.width = 52
                    player2.hit = False
                    player2.animHit = 0

def checkTouch(attackPlayer,defPlayer):
    return checkCollision(attackPlayer, defPlayer)


# def checkTouch(attackPlayer,defPlayer):
#     pl1=boxActiveUnion(attackPlayer)
#     pl2=boxActiveUnion(defPlayer)
#     if pl1[0].isdisjoint(pl2[0]):
#         return False
#     else:
#         return True


