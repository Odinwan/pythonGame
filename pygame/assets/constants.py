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

walk1 = [pygame.image.load('images/png/Run__000.png'),
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

player_img = pygame.image.load("images/png/Idle__000.png")

walk2 = [pygame.transform.scale(pygame.image.load('images/png2/Run__000.png'),(71,90)),
                pygame.transform.scale(pygame.image.load('images/png2/Run__001.png'),(71,90)),
                pygame.transform.scale(pygame.image.load('images/png2/Run__002.png'),(71,90)),
                pygame.transform.scale(pygame.image.load('images/png2/Run__003.png'),(71,90)),
                pygame.transform.scale(pygame.image.load('images/png2/Run__004.png'),(71,90)),
                pygame.transform.scale(pygame.image.load('images/png2/Run__005.png'),(71,90)),
                pygame.transform.scale(pygame.image.load('images/png2/Run__006.png'),(71,90)),
                pygame.transform.scale(pygame.image.load('images/png2/Run__007.png'),(71,90)),
                pygame.transform.scale(pygame.image.load('images/png2/Run__008.png'),(71,90)),
                pygame.transform.scale(pygame.image.load('images/png2/Run__009.png'),(71,90)),
                ]

player2Stand = pygame.image.load("images/png2/Idle__000.png")

player2_rect = player2Stand.get_rect()
bg = pygame.image.load("images/USn6ve.jpg")
