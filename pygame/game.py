import pygame
import math

pygame.init()
height = 500
width = 500
clock = pygame.time.Clock()
win = pygame.display.set_mode((height,width))

pygame.display.set_caption('Cubes Game')
run = True

walkRight1 = [pygame.image.load('images/bartRight1-1.png'),
                pygame.image.load('images/bartRight1-2.png'),
                pygame.image.load('images/bartRight1-3.png'),
                pygame.image.load('images/bartRight1-4.png'),
                pygame.image.load('images/bartRight1-5.png'),
                pygame.image.load('images/bartRight1-6.png')]

walkLeft1 = [pygame.image.load('images/bartLeft1-1.png'),
                pygame.image.load('images/bartLeft1-2.png'),
                pygame.image.load('images/bartLeft1-3.png'),
                pygame.image.load('images/bartLeft1-4.png'),
                pygame.image.load('images/bartLeft1-5.png'),
                pygame.image.load('images/bartLeft1-6.png')]

player1Stand = pygame.image.load("images/bartLeft1-3.png")

walkRight2 = [pygame.image.load('images/bartRight2-1.png'),
                pygame.image.load('images/bartRight2-2.png'),
                pygame.image.load('images/bartRight2-3.png'),
                pygame.image.load('images/bartRight2-4.png'),
                pygame.image.load('images/bartRight2-5.png'),
                pygame.image.load('images/bartRight2-6.png')]

walkLeft2 = [pygame.image.load('images/bartLeft2-1.png'),
                pygame.image.load('images/bartLeft2-2.png'),
                pygame.image.load('images/bartLeft2-3.png'),
                pygame.image.load('images/bartLeft2-4.png'),
                pygame.image.load('images/bartLeft2-5.png'),
                pygame.image.load('images/bartLeft2-6.png')]

player2Stand = pygame.image.load("images/bartLeft2-3.png")
bg = pygame.image.load("images/USn6ve.jpg")

class players:
     def __init__(self, x ,y ,width ,height,leftImage,rightImage,playerStand):
         self.x = x
         self.y = y
         self.width = width
         self.height = height
         self.walkRight = rightImage
         self.walkLeft = leftImage
         self.playerStand = playerStand
         self.speed = 5
         self.jump = False
         self.jumpCount = 0
         self.left = False
         self.right = False
         self.animCount = 0
         
def drowWindow():
    win.blit(bg,(0,0))
    animationFrame(player1)
    animationFrame(player2)
    pygame.display.update()
    

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

touch = False
player2 = players(int(width - (width * 0.1)),390,60,120,walkLeft2,walkRight2,player2Stand)
player1 = players(int(width - (width * 0.9)),390,60,120,walkLeft1,walkRight1,player1Stand)


while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pl1=V(player1)
    pl2=V(player2)
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and player1.x > 2:
        if not touch:
            if not player1.left:
                player1.speed = 0
            player1.speed -= 1
            player1.x += player1.speed
            player1.left = True
            player1.right = False
    elif keys[pygame.K_d] and player1.x < (width - player1.width - 2):
        if not touch:
            if not player1.right:
                player1.speed = 0
            player1.speed += 1
            player1.x += player1.speed
            player1.left = False
            player1.right = True
    else:
        player1.left = False
        player1.right = False
        player1.speed = 0
    if not(player1.jump):
        if keys[pygame.K_LSHIFT]:
            player1.jump = True
    else:
        if player1.jumpCount < 15:
            player1.jumpCount += 1
            player1.y -= 1
        elif player1.jumpCount >= 15 and player1.jumpCount <= 29:
            player1.jumpCount += 1
            player1.y += 1
            print(player1.jumpCount)
        elif player1.jumpCount >= 30:
            player1.jumpCount = 0
            player1.jump = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player2.x > 2:
        if not touch:        
            if not player2.left:
                player2.speed = 0
            player2.speed -= 1
            player2.x += player2.speed
            player2.left = True
            player2.right = False
    elif keys[pygame.K_RIGHT] and player2.x < (width - player2.width - 2):
        if not touch:
            if not player2.right:
                player2.speed = 0
            player2.speed += 1
            player2.x += player2.speed
            player2.left = False
            player2.right = True
    else :
        player2.left = False
        player2.right = False
        player2.speed = 0
    if not(player2.jump):
        if keys[pygame.K_SPACE]:
            player2.jump = True
    else:
        if player2.jumpCount < 15:
            player2.jumpCount += 1
            player2.y -= 1
        elif player2.jumpCount >= 15 and player2.jumpCount <= 29:
            player2.jumpCount += 1
            player2.y += 1
            print(player2.jumpCount)
        elif player2.jumpCount >= 30:
            player2.jumpCount = 0
            player2.jump = False
            
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
        print('pervaya ' + str(player1.speed))
        print('vtoraya ' + str(player2.speed))
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
            print('ravno')
            player2.x -= (player2.speed+1)*5
            player1.x -= (player1.speed+1)*5
    drowWindow()

pygame.quit()
