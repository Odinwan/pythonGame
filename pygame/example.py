import pygame
import random

pygame.init()

WIDTH = 500
HEIGHT = 500
clock = pygame.time.Clock()
bg = pygame.Surface((WIDTH,HEIGHT))
run = True
RED = (152,0,2)
win = pygame.display.set_mode((WIDTH,HEIGHT))
win.blit(bg,(0,0))

class Herovina(pygame.sprite.Sprite):
    def __init__(self, ):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((60, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        #self.rect.x = WIDTH // 2 
        self.rect.y = HEIGHT - 40
        self.rect.centerx = WIDTH // 2
        self.rect.top = self.rect.y
        self.speed = 0

    def update(self):
        self.speed = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.speed -= 2
        if keys[pygame.K_d]:
            self.speed += 3

        if self.speed > 6 :
            self.speed = 6
        if self.speed < -6:
            self.speed = -6
        self.rect.x += self.speed
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    def shoot(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            bullet = shot(self.rect.centerx, self.rect.top)
            All_sprites.add(bullet)
            Bullets.add(bullet)

class shot(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.y = y + 5 
        self.rect.centerx = x
        
    
    def update(self):
        self.rect.y -= 10
        if self.rect.y < 0:
            self.kill()

class drop(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(-70, -50)
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.speedx = random.randrange(-5,5)
        self.speedy = random.randrange(3,5)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top == HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH +20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-70, -50)
            self.speedy = random.randrange(3,5)


her = Herovina()


meteors = pygame.sprite.Group()
All_sprites = pygame.sprite.Group()
Bullets = pygame.sprite.Group()
All_sprites.add(her)
for i in range(10):    
    drop1 = drop()
    All_sprites.add(drop1)
    meteors.add(drop1)


    

while run:
    clock.tick(60)
    win.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                her.shoot()
    hits = pygame.sprite.groupcollide(meteors, Bullets, True, True)
    for hit in hits:
        drop1 = drop()
        All_sprites.add(drop1)
        meteors.add(drop1)
    hits = pygame.sprite.spritecollide(her, meteors, False)
    if hits:
        running = False

    All_sprites.update()
    All_sprites.draw(win)

    pygame.display.update()

pygame.quit()