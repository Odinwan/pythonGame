import pygame

from assets.constants import *

class players(pygame.sprite.Sprite):
    def __init__(self, x ,y , imagesIdle , imagesWalk,imagesAttack,imagesJump,number):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.transform.scale(imagesIdle[0], (52, 90))
        self.playerStand = pygame.Surface((52,90))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.number = number
        self.speed = 1

        self.left = False
        self.right = False
        self.hit = False
        self.jump = False

        self.imagesAttack = imagesAttack
        self.imagesWalk = imagesWalk
        self.imagesIdle = imagesIdle
        self.imagesJump = imagesJump

        self.position = 'left'
        self.actionType = 'stay'

        self.animCount = 0
        self.jumpCount = 0
        self.jumpValue = 5
        self.attackCount = 0
        self.walkCount = 0


class lifes:
     def __init__(self, x, width, number):
         self.x = x
         self.y = 10
         self.width = width
         self.height = 20
         self.number = number 

class simpleAttack(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = pygame.Surface((52,90))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = GREEN

    def draw(self,window): 
        pygame.draw.rect(window, self.color, pygame.Rect( self.rect.x, self.rect.y, self.rect.width, self.rect.height))

