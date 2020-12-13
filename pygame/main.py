import pygame
import math

from assets.constants import *
from modules.players import *
from actions.move import *
from actions.touchAction import *
from actions.action import *
from actions.default import *

pygame.init()

members = []

members.append(players(int(width - (width * 0.2)),390,firstStay,firstWalk,firstAttack,firstJump,0))
members.append(players(int(width - (width * 0.9)),390,secondStay,secondWalk,secondAttack,secondJump,1))

def drowWindow():

    win.blit(bg,(0,0))

    for player in members:
        allAnimationSwich(player)
        actionPlayer(player,touch,win,members.index(player))
        checkBorder(player)
        checkAttack(player)

    checkPosition(members[0],members[1])

    pygame.display.update()

while run:

    clock.tick(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    drowWindow()

pygame.quit()
