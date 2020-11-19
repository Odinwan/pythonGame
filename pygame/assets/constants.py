import pygame

height = 500
width = 500
clock = pygame.time.Clock()
win = pygame.display.set_mode((height,width))

pygame.display.set_caption('Cubes Game')
run = True
touch = False

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
