import math
from modules.players import *
from assets.constants import *


def CheckLife(life,numb,value):
    if numb == 2:
        if life.width != 0:
            life.width -= 30
            life.x += 30
    else:
        if life.width != 0:
            life.width -= 30   
    
def checkCollision( player1, player2):
    col = pygame.sprite.collide_rect(player1, player2)
     
    return col