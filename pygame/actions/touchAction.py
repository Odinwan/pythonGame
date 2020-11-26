import math
from modules.players import *
from assets.constants import *

def touchAction(player1,player2,touch):
    pl1=V(player1)
    pl2=V(player2)

    if pl1[0].isdisjoint(pl2[0]):
        return False
    else:
        return True

def CheckLife(life1,life2):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_g]:
        life2.width -= 30
        life2.x += 30
    if  keys[pygame.K_l]:
        life1.width -= 30   

def checkCollision(self, player1, player2):
    col = pygame.sprite.collide_rect(player1, player2)
    return col