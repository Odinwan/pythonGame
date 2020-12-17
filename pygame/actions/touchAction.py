import math
from modules.players import *
from assets.constants import *


def CheckLife(life,numb,value):
    if numb == 2:
        life.width -= 30
        life.x += 30
    else:
        life.width -= 30   
    
def checkCollision( player1, player2): return pygame.sprite.collide_rect(player1, player2)