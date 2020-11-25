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

    
        # if math.fabs(player1.speed) > math.fabs(player2.speed):
        #     player1.speed = player1.speed // 2
        #     player1.x -= (player1.speed+1)*5
        #     if player1.right == True:
        #         player2.x += 5
        #     else:
        #         player2.x -= 5
        # elif math.fabs(player1.speed) < math.fabs(player2.speed):
        #     player2.speed = player2.speed // 2
        #     player2.x -= (player2.speed+1)*5
        #     if player2.right == True:
        #         player1.x += 5
        #     else:
        #         player1.x -= 5
        # elif (math.fabs(player1.speed) == math.fabs(player2.speed)) and (player1.speed != 0):
        #     player2.speed = player2.speed // 2
        #     player1.speed = player1.speed // 2 
        #     player2.x -= (player2.speed+1)*5
        #     player1.x -= (player1.speed+1)*5