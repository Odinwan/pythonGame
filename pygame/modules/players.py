import pygame
from assets.constants import *
class players(pygame.sprite.Sprite):
    def __init__(self, x ,y , player_img , leftImage,rightImage ,number):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (52, 90))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
        self.walkRight = rightImage
        self.walkLeft = leftImage
        self.playerStand = pygame.Surface((52,90))
        self.speed = 1
        self.jump = False
        self.jumpCount = 0
        self.hit = False
        self.left = False
        self.right = False
        self.animCount = 0
        self.animHit = 0
        self.number = number
        self.widthBoxAction = 52 
        self.heightBoxAction = 90 
         
class lifes:
     def __init__(self, x, width, number):
         self.x = x
         self.y = 10
         self.width = width
         self.height = 20
         self.number = number

def V(player):
    x1 = player.rect.x
    x2 = player.rect.x + player.rect.get_width()
    y1 = player.rect.y
    y2 = player.rect.y + player.rect.get_height()
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
    x1 = box.rect.x
    x2 = box.rect.x + box.widthBoxAction
    y1 = box.rect.y
    y2 = box.rect.y + box.heightBoxAction
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
    return pygame.draw.rect(win, (255,0,0) , pygame.Rect(player.rect.x , player.rect.y , player.widthBoxAction , player.heightBoxAction),  2) 