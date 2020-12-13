import pygame
from assets.constants import *

def allAnimationSwich(player):
    if player.animCount + 1 >= 50:
        player.animCount = 0

    if (player.actionType == 'walk'): walkPlayer(player)
    elif (player.actionType == 'attack'): attackPlayer(player)
    elif (player.actionType == 'jump'): jumpPlayer(player)
    else: stayPlayer(player)

def attackPlayer(player):
    if player.position == 'right': win.blit(player.imagesAttack[player.attackCount // 2],(player.rect.x,player.rect.y))
    elif player.position == 'left': win.blit(pygame.transform.flip(player.imagesAttack[player.attackCount // 2],True,False),(player.rect.x - 30,player.rect.y))


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
        win.blit(pygame.transform.flip(player.imagesJump[player.animCount // 5],True,False),(player.rect.x,player.rect.y))
        player.animCount += 1
    elif player.position == 'right':
        win.blit(player.imagesJump[player.animCount // 5],(player.rect.x,player.rect.y))
        player.animCount += 1
