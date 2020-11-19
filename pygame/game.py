import pygame
import math
from assets.constants import *
from modules.players import *
from actions.move import *

pygame.init()
      
def drowWindow():
    win.blit(bg,(0,0))
    animationFrame(player1)
    animationFrame(player2)
    pygame.display.update()
    
player2 = players(int(width - (width * 0.1)),390,60,120,walkLeft2,walkRight2,player2Stand,2)
player1 = players(int(width - (width * 0.9)),390,60,120,walkLeft1,walkRight1,player1Stand,1)

def animationFrame(player):
    if player.animCount + 1 >= 30:
        player.animCount = 0
    if player.left:
        win.blit(player.walkLeft[player.animCount // 5],(player.x,player.y))
        player.animCount += 1
    elif player.right:
        win.blit(player.walkRight[player.animCount // 5],(player.x,player.y))
        player.animCount += 1
    else :
        win.blit(player.playerStand,(player.x,player.y))
        player.animCount = 0

while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pl1=V(player1)
    pl2=V(player2)
    
    move(player1)
    move(player2)
            
    if player1.speed >= 7:
        player1.speed = 7
    if player2.speed >= 7:
        player2.speed = 7
    if player1.speed <= -7:
        player1.speed = -7
    if player2.speed <= -7:
        player2.speed = -7
    if pl1[0].isdisjoint(pl2[0]):
        touch = False
    else:
        touch = True
        if math.fabs(player1.speed) > math.fabs(player2.speed):
            player1.speed = player1.speed // 2
#             player2.x -= (player2.speed+1)*10
            player1.x -= (player1.speed+1)*5
            if player1.right == True:
                player2.x += 5
            else:
                player2.x -= 5
#             if player1.left == True:
#                 player2.speed = -2
#             else:
#                 player2.speed = 2
        elif math.fabs(player1.speed) < math.fabs(player2.speed):
            player2.speed = player2.speed // 2
#             player1.x -= (player1.speed+1)*10
            player2.x -= (player2.speed+1)*5
            if player2.right == True:
                player1.x += 5
            else:
                player1.x -= 5
#             if player2.left == True:
#                 player1.speed = -2
#             else:
#                 player1.speed = 2

        elif (math.fabs(player1.speed) == math.fabs(player2.speed)) and (player1.speed != 0):
            player2.speed = player2.speed // 2
            player1.speed = player1.speed // 2 
            player2.x -= (player2.speed+1)*5
            player1.x -= (player1.speed+1)*5
    drowWindow()

pygame.quit()
