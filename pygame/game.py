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
    createActionBox(player1)
    createActionBox(player2)
    checkBorder(player1)
    checkBorder(player2)
    createLifeBoxDamaged1()
    createLifeBox1(lifeBox1)
    createLifeBoxDamaged2()
    createLifeBox2(lifeBox2)
    pygame.display.update()


player1 = players(int(width - (width * 0.9)),390,60,120,walkLeft1,walkRight1,player1Stand,1)
player2 = players(int(width - (width * 0.1)),390,60,120,walkLeft2,walkRight2,player2Stand,2)
lifeBox1 = lifes(10, 220,1)
lifeBox2 = lifes((height - 230), 220,2)

def createLifeBox1(life):
    pygame.draw.rect(win, GREEN , (life.x, life.y, life.width, life.height) )

def createLifeBoxDamaged1():
    pygame.draw.rect(win, RED ,(10, 10, 220, 20) ) 

def createLifeBox2(life):
    pygame.draw.rect(win, GREEN , (life.x, life.y, life.width, life.height) )

def createLifeBoxDamaged2():
    pygame.draw.rect(win, RED ,((height - 230),10 ,220 ,20 ) ) 

def animationFrame(player):
    if player.animCount + 1 >= 30:
        player.animCount = 0

    if not(touch):
        if player.left:
            win.blit(player.walkLeft[player.animCount // 5],(player.x,player.y))
            player.animCount += 1
        elif player.right:
            win.blit(player.walkRight[player.animCount // 5],(player.x,player.y))
            player.animCount += 1
        else :
            win.blit(player.playerStand,(player.x,player.y))
            player.animCount = 0
    else :
        win.blit(player.playerStand,(player.x,player.y))
        player.animCount = 0

while run:
    clock.tick(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # touch = touchAction(player1,player2,touch)
    CheckLife(lifeBox1,lifeBox2)
    move(player1,touch)
    move(player2,touch)
    hit(player1,player2)

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
