import pygame
from assets.constants import *

def allAnimationSwich(player,box):
    if player.animCount + 1 >= 50:
        player.animCount = 0
    if (player.actionType == 'shock'): shockPlayer(player)
    elif (player.actionType == 'walk'): walkPlayer(player)
    elif (player.actionType == 'attack'): attackPlayer(player, box)
    elif (player.actionType == 'jump'): jumpPlayer(player)
    else: stayPlayer(player)

    drawBox(box)

def attackPlayer(player, box):
    if player.position == 'right': win.blit(player.imagesAttack[player.attackCount // 2],(player.rect.x,player.rect.y))
    elif player.position == 'left': win.blit(pygame.transform.flip(player.imagesAttack[player.attackCount // 2],True,False),(player.rect.x - 30,player.rect.y))
    animAtackBox(box)

def walkPlayer(player):
    if not(touch):
        if player.left:
            win.blit(pygame.transform.flip(player.imagesWalk[player.animCount // 5],True,False),(player.rect.x,player.rect.y))
            player.animCount += 1
        elif player.right:
            win.blit(player.imagesWalk[player.animCount // 5],(player.rect.x,player.rect.y))
            player.animCount += 1

def stayPlayer(player):
    if player.position == 'right':
        win.blit(player.imagesIdle[player.animCount // 5],(player.rect.x,player.rect.y))
        player.animCount += 1
    else:
        win.blit(pygame.transform.flip(player.imagesIdle[player.animCount // 5],True,False),(player.rect.x,player.rect.y))
        player.animCount += 1

def jumpPlayer(player):
    if player.position == 'left':
        win.blit(pygame.transform.flip(player.imagesJump[player.jumpCount // 6],True,False),(player.rect.x,player.rect.y))
    elif player.position == 'right':
        win.blit(player.imagesJump[player.jumpCount // 6],(player.rect.x,player.rect.y))

def shockPlayer(player):
    if player.position == 'left':
        win.blit(pygame.transform.flip(player.imageShock,True,False),(player.rect.x,player.rect.y))
    elif player.position == 'right':
        win.blit(player.imageShock,(player.rect.x,player.rect.y))
#boxes
def drawBox(box):
    pygame.draw.rect(win, RED ,(box.rect.x, box.rect.y, box.rect.width, box.rect.height),2 )

def animAtackBox(box):
    if box.animCount <= 18:
        box.animCount += 1
    else:
        box.animCount = 0