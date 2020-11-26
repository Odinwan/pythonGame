import pygame
from assets.constants import *
class players(pygame.sprite.Sprite):
    def __init__(self, x ,y , player_img , leftImage,rightImage ,number):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (52, 90))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
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
        
         
class lifes:
     def __init__(self, x, width, number):
         self.x = x
         self.y = 10
         self.width = width
         self.height = 20
         self.number = number

