import pygame
import math

from assets.constants import *
from modules.players import *
from actions.physicalAction import *
from actions.touchAction import *
from actions.animationActions import *
from actions.commonState import *

pygame.init()

members = []

members.append(players(int(width - (width * 0.2)),480,firstStay,firstWalk,firstAttack,firstJump,0))
members.append(players(int(width - (width * 0.9)),480,secondStay,secondWalk,secondAttack,secondJump,1))

def createLifeBox1(life):
    pygame.draw.rect(win, GREEN , (life.x, life.y, life.width, life.height) )

def createLifeBoxDamaged1():
    pygame.draw.rect(win, RED ,(10, 10, 300, 20) )

def createLifeBox2(life):
    pygame.draw.rect(win, GREEN , (life.x, life.y, life.width, life.height) )

def createLifeBoxDamaged2():
    pygame.draw.rect(win, RED ,((width - 310),10 ,300 ,20 ) )

lifeBox1 = lifes(10, 300,1)
lifeBox2 = lifes((width - 310), 300,2)

def drowWindow():

    win.blit(bg,(0,0))

    createLifeBoxDamaged1()
    createLifeBox1(lifeBox1)
    createLifeBoxDamaged2()
    createLifeBox2(lifeBox2)

    for player in members:
        allAnimationSwich(player)
        physicalAction(player,touch,win,members.index(player))
        checkBorder(player)
        checkAttack(player)

    checkPosition(members[0],members[1])
    GameOver(lifeBox1,lifeBox2)
    pygame.display.update()

def GameOver(life1,life2):
    if (life1.width == 0) or (life2.width == 0):
        win.blit(go,(0,0))

while run:

    clock.tick(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    drowWindow()

pygame.quit()
