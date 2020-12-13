import pygame
from assets.constants import *
class players(pygame.sprite.Sprite):
    def __init__(self, x ,y , player_img , walk,jump_anim,idle,number):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(player_img, (52, 90))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # self.hitBoxRect.x = self.rect.x
        # self.hitBoxRect.y = self.rect.y
        self.walk = walk
        self.playerStand = pygame.Surface((52,90))
        self.speed = 1
        self.jump = False
        self.jump_amim = jump_anim
        self.idle = idle
        self.position = 'left'
        self.jumpCount = 0
        self.hit = False
        self.left = False
        self.right = False
        self.animCount = 0
        self.animHit = 0
        self.number = number
        self.dead = False
    def Strike(self):
        HitBox = HitBoxes(self.rect.width, self.rect.height)
        hb.add(HitBox)

class HitBoxes(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((x, y))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.count = 0
        self.grow = True
        
    def update(self):
        print(self.count)
        if self.count >= 14 or self.grow == False:
            self.count -= 1
            self.rect.width -= 5
            self.grow = False
            if self.count == 0:
                self.kill()
        elif  self.grow == True:
            self.count += 1
            self.rect.width += 5


class lifes:
     def __init__(self, x, width, number):
         self.x = x
         self.y = 10
         self.width = width
         self.height = 20
         self.number = number

