import pygame

height = 500
width = 500
clock = pygame.time.Clock()
win = pygame.display.set_mode((height,width))
GREEN = (0, 200, 64)
RED = (152,0,2)
pygame.display.set_caption('Cubes Game')
run = True
touch = False

walkRight1 = [pygame.image.load('images/png/Run__000.png'),
                pygame.image.load('images/png/Run__001.png'),
                pygame.image.load('images/png/Run__002.png'),
                pygame.image.load('images/png/Run__003.png'),
                pygame.image.load('images/png/Run__004.png'),
                pygame.image.load('images/png/Run__005.png'),
                pygame.image.load('images/png/Run__006.png'),
                pygame.image.load('images/png/Run__007.png'),
                pygame.image.load('images/png/Run__008.png'),
                pygame.image.load('images/png/Run__009.png')
                ]

walkLeft1 = [pygame.image.load('images/png/Run__000Left.png'),
                pygame.image.load('images/png/Run__001Left.png'),
                pygame.image.load('images/png/Run__002Left.png'),
                pygame.image.load('images/png/Run__003Left.png'),
                pygame.image.load('images/png/Run__004Left.png'),
                pygame.image.load('images/png/Run__005Left.png'),
                pygame.image.load('images/png/Run__006Left.png'),
                pygame.image.load('images/png/Run__007Left.png'),
                pygame.image.load('images/png/Run__008Left.png'),
                pygame.image.load('images/png/Run__009Left.png')]

player_img = pygame.image.load("images/png/Idle__000.png")

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
player2_rect = player2Stand.get_rect()
bg = pygame.image.load("images/USn6ve.jpg")
