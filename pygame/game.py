import pygame
import math
from assets.constants import *
from modules.players import *
from actions.move import *
from actions.touchAction import *

pygame.init()

def drowWindow():
    win.blit(bg,(0,0))
    animationFrame(player1)
    animationFrame(player2)
    checkBorder(player1)
    checkBorder(player2)
    createLifeBoxDamaged1()
    createLifeBox1(lifeBox1)
    createLifeBoxDamaged2()
    createLifeBox2(lifeBox2)
    hb.draw(win)

    GameOver(lifeBox1,lifeBox2)
    pygame.display.update()


player1 = players(int(width - (width * 0.9)),390, player_img,walk1,jump1,idle1,1)
player2 = players(int(width - (width * 0.1)),390, player2Stand,walk2,jump2,idle2,2)


lifeBox1 = lifes(10, 300,1)
lifeBox2 = lifes((width - 310), 300,2)


def GameOver(life1,life2):
    if (life1.width == 0) or (life2.width == 0):
        win.blit(go,(0,0))

def createLifeBox1(life):
    pygame.draw.rect(win, GREEN , (life.x, life.y, life.width, life.height) )

def createLifeBoxDamaged1():
    pygame.draw.rect(win, RED ,(10, 10, 300, 20) )

def createLifeBox2(life):
    pygame.draw.rect(win, GREEN , (life.x, life.y, life.width, life.height) )

def createLifeBoxDamaged2():
    pygame.draw.rect(win, RED ,((width - 310),10 ,300 ,20 ) )

def createHitBox(HitBox):
    pygame.draw.rect(win, GREEN , (HitBox.rect.x, HitBox.rect.y, HitBox.rect.width, HitBox.rect.height),1 )

def checkPosition(player1,player2):
    if (player1.rect.x >= player2.rect.x):
        player1.position = 'left'
        player2.position = 'right'
    else:
        player2.position = 'left'
        player1.position = 'right'


def animationFrame(player):
    if player.animCount + 1 >= 30:
        player.animCount = 0

    if not(touch):
        #Jump Animation
        if player.jump: 
            if player.position == 'left':
                win.blit(pygame.transform.flip(player.jump_amim[player.animCount // 20],True,False),(player.rect.x,player.rect.y))
                player.animCount += 1
            elif player.position == 'right':
                win.blit(player.jump_amim[player.animCount // 20],(player.rect.x,player.rect.y))
                player.animCount += 1
        #left move animation
        else:
            if player.left:
                win.blit(pygame.transform.flip(player.walk[player.animCount // 5],True,False),(player.rect.x,player.rect.y))
                player.animCount += 1
            #right move animation
            elif player.right:
                win.blit(player.walk[player.animCount // 5],(player.rect.x,player.rect.y))
                player.animCount += 1
            else :
                #idle animation  R
                if player.position == 'right':
                    win.blit(player.idle[player.animCount // 5],(player.rect.x,player.rect.y))
                    player.animCount += 1
                #idle animation L
                else:
                    win.blit(pygame.transform.flip(player.idle[player.animCount // 5],True,False),(player.rect.x,player.rect.y))
                    player.animCount += 1
    

    #idle Anim ????
    else :
        if player.position == 'right':
            win.blit(player.idle[player.animCount // 5],(player.rect.x,player.rect.y))
            player.animCount += 1
        else:
            win.blit(pygame.transform.flip(player.idle[player.animCount // 5],True,False),(player.rect.x,player.rect.y))
            player.animCount += 1
        player.animCount = 0

    



while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    move(player1,touch)
    move(player2,touch)
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
