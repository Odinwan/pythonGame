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

def CheckLife(life,numb,value):
    if numb == 2:
        life.width -= 30
        life.x += 30
    else:
        life.width -= 30   
    
def checkCollision( player1, player2):
    col = pygame.sprite.collide_rect(player1, player2)
     
    return col