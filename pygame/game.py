import pygame
import math
from assets.constants import *
from modules.players import *
from actions.move import *
from actions.touchAction import *

pygame.init()

def drowWindow():
    win.blit(bg,(0,0))
    allAnimationSwich(player1)
    allAnimationSwich(player2)
    checkBorder(player1)
    checkBorder(player2)
    createLifeBoxDamaged1()
    createLifeBox1(lifeBox1)
    createLifeBoxDamaged2()
    createLifeBox2(lifeBox2)
    pygame.display.update()


player1 = players(int(width - (width * 0.9)),390, player_img,walk1,1,attack1)
player2 = players(int(width - (width * 0.1)),390, player2Stand,walk2,2,attack2)
lifeBox1 = lifes(10, 220,1)
lifeBox2 = lifes((height - 230), 220,2)

plr2 = pygame.sprite.Group()
plr2.add(player2)

def createLifeBox1(life):
    pygame.draw.rect(win, GREEN , (life.x, life.y, life.width, life.height) )

def createLifeBoxDamaged1():
    pygame.draw.rect(win, RED ,(10, 10, 220, 20) )

def createLifeBox2(life):
    pygame.draw.rect(win, GREEN , (life.x, life.y, life.width, life.height) )

def createLifeBoxDamaged2():
    pygame.draw.rect(win, RED ,((height - 230),10 ,220 ,20 ) )

def checkPosition(player1,player2):
    if (player1.rect.x >= player2.rect.x):
        player1.position = 'left'
        player2.position = 'right'
    else:
        player2.position = 'left'
        player1.position = 'right'

def allAnimationSwich(player):
    p = pygame.draw.rect(win, GREEN, pygame.Rect( player.rect.x ,player.rect.y, player.rect.width, player.rect.height))
    p.x
    if player.animCount + 1 >= 30:
        player.animCount = 0

    if (player.actionType == 'walk'):
        walkPlayer(player)
    elif (player.actionType == 'attack'):  
        attackPlayer(player)
    else: stayPlayer(player)

def attackPlayer(player):
    if player.position == 'right':
        win.blit(player.attack[player.animCount // 5],(player.rect.x,player.rect.y))
    elif player.position == 'left':
        win.blit(pygame.transform.flip(player.attack[player.animCount // 5],True,False),(player.rect.x - 30,player.rect.y))

def walkPlayer(player):
    if not(touch):
        if player.left:
            win.blit(pygame.transform.flip(player.walk[player.animCount // 5],True,False),(player.rect.x,player.rect.y))
            player.animCount += 1
        elif player.right:
            win.blit(player.walk[player.animCount // 5],(player.rect.x,player.rect.y))
            player.animCount += 1

def stayPlayer(player):
    if player.position == 'right':
        win.blit(player.image,(player.rect.x,player.rect.y))
    else:
        win.blit(pygame.transform.flip(player.image,True,False),(player.rect.x,player.rect.y))

while run:
    clock.tick(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    move(player1,touch,win)
    move(player2,touch,win)
    checkPosition(player1,player2)
    hit(player1,player2, lifeBox1, lifeBox2)
    if player1.speed >= 4:
        player1.speed = 4
    if player2.speed >= 4:
        player2.speed = 4
    if player1.speed <= -4:
        player1.speed = -4
    if player2.speed <= -4:
        player2.speed = -4

    drowWindow()

pygame.quit()
