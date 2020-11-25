import pygame
from assets.constants import *
class players:
    def __init__(self, x ,y ,width ,height,leftImage,rightImage,playerStand,number):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkRight = rightImage
        self.walkLeft = leftImage
        self.playerStand = playerStand
        self.speed = 1
        self.jump = False
        self.jumpCount = 0
        self.hit = False
        self.left = False
        self.right = False
        self.animCount = 0
        self.animHit = 0
        self.number = number
        self.widthBoxAction = width + 30
        self.heightBoxAction = height + 30

def V(player):
    x1 = player.x
    x2 = player.x + player.width
    y1 = player.y
    y2 = player.y + player.height
    xx = set()
    yy = set()
    for i in range(x1,x2):
        xx.add(i)
    for i in range(y1,y2):
        yy.add(i)
    list = []
    list.append(xx)
    list.append(yy)
    return list

def boxActiveUnion(box):
    x1 = box.x
    x2 = box.x + box.widthBoxAction
    y1 = box.y
    y2 = box.y + box.heightBoxAction
    xx = set()
    yy = set()
    for i in range(x1,x2):
        xx.add(i)
    for i in range(y1,y2):
        yy.add(i)
    list = []
    list.append(xx)
    list.append(yy)
    return list

def createActionBox(player):
    return pygame.draw.rect(win, (255,0,0) , pygame.Rect(player.x - 25, player.y , player.widthBoxAction , player.heightBoxAction),  2) 