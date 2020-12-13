import pygame

height = 600
width = 800
clock = pygame.time.Clock()
win = pygame.display.set_mode((width,height))
GREEN = (0, 200, 64)
RED = (152,0,2)
pygame.display.set_caption('Cubes Game')
run = True
touch = False
hb = pygame.sprite.Group()

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

# player1Stand =pygame.transform.scale("images/png/Idle__000.png", (50, 38))


walk2 = [pygame.transform.scale(pygame.image.load('images/png2/Run__000.png'),(71,90)),
        pygame.transform.scale(pygame.image.load('images/png2/Run__001.png'),(71,90)),
        pygame.transform.scale(pygame.image.load('images/png2/Run__002.png'),(71,90)),
        pygame.transform.scale(pygame.image.load('images/png2/Run__003.png'),(71,90)),
        pygame.transform.scale(pygame.image.load('images/png2/Run__004.png'),(71,90)),
        pygame.transform.scale(pygame.image.load('images/png2/Run__005.png'),(71,90)),
        pygame.transform.scale(pygame.image.load('images/png2/Run__006.png'),(71,90)),
        pygame.transform.scale(pygame.image.load('images/png2/Run__007.png'),(71,90)),
        pygame.transform.scale(pygame.image.load('images/png2/Run__008.png'),(71,90)),
                ]

idle1 = [pygame.transform.scale(pygame.image.load('images/png/Idle__000.png'),(52,90)),
        pygame.transform.scale(pygame.image.load('images/png/Idle__001.png'),(52,90)),
        pygame.transform.scale(pygame.image.load('images/png/Idle__002.png'),(52,90)),
        pygame.transform.scale(pygame.image.load('images/png/Idle__003.png'),(52,90)),
        pygame.transform.scale(pygame.image.load('images/png/Idle__004.png'),(52,90)),
        pygame.transform.scale(pygame.image.load('images/png/Idle__005.png'),(52,90)),
        pygame.transform.scale(pygame.image.load('images/png/Idle__006.png'),(52,90)),
        pygame.transform.scale(pygame.image.load('images/png/Idle__007.png'),(52,90)),
        pygame.transform.scale(pygame.image.load('images/png/Idle__008.png'),(52,90)),
        pygame.transform.scale(pygame.image.load('images/png/Idle__009.png'),(52,90)),
        ]  
idle2 = [pygame.transform.scale(pygame.image.load('images/png2/Idle__000.png'),(52,90)),
        pygame.transform.scale(pygame.image.load('images/png2/Idle__001.png'),(52,90)),
        pygame.transform.scale(pygame.image.load('images/png2/Idle__002.png'),(52,90)),
        pygame.transform.scale(pygame.image.load('images/png2/Idle__003.png'),(52,90)),
        pygame.transform.scale(pygame.image.load('images/png2/Idle__004.png'),(52,90)),
        pygame.transform.scale(pygame.image.load('images/png2/Idle__005.png'),(52,90)),
        pygame.transform.scale(pygame.image.load('images/png2/Idle__006.png'),(52,90)),
        pygame.transform.scale(pygame.image.load('images/png2/Idle__007.png'),(52,90)),
        pygame.transform.scale(pygame.image.load('images/png2/Idle__008.png'),(52,90)),
        pygame.transform.scale(pygame.image.load('images/png2/Idle__009.png'),(52,90)),
        ] 

jump2 = [pygame.transform.scale(pygame.image.load('images/png2/Jump__000.png'),(71,90)),
        pygame.transform.scale(pygame.image.load('images/png2/Jump__001.png'),(71,90)),
        pygame.transform.scale(pygame.image.load('images/png2/Jump__002.png'),(71,90)),
        pygame.transform.scale(pygame.image.load('images/png2/Jump__003.png'),(71,90)),
        pygame.transform.scale(pygame.image.load('images/png2/Jump__004.png'),(71,90)),
        pygame.transform.scale(pygame.image.load('images/png2/Jump__005.png'),(71,90)),
        pygame.transform.scale(pygame.image.load('images/png2/Jump__006.png'),(71,90)),
        pygame.transform.scale(pygame.image.load('images/png2/Jump__007.png'),(71,90)),
        pygame.transform.scale(pygame.image.load('images/png2/Jump__008.png'),(71,90)),
        pygame.transform.scale(pygame.image.load('images/png2/Jump__009.png'),(71,90)),
                ]
jump1 = [pygame.transform.scale(pygame.image.load('images/png/Jump__000.png'),(71,90)),
        pygame.transform.scale(pygame.image.load('images/png/Jump__001.png'),(71,90)),
        pygame.transform.scale(pygame.image.load('images/png/Jump__002.png'),(71,90)),
        pygame.transform.scale(pygame.image.load('images/png/Jump__003.png'),(71,90)),
        pygame.transform.scale(pygame.image.load('images/png/Jump__004.png'),(71,90)),
        pygame.transform.scale(pygame.image.load('images/png/Jump__005.png'),(71,90)),
        pygame.transform.scale(pygame.image.load('images/png/Jump__006.png'),(71,90)),
        pygame.transform.scale(pygame.image.load('images/png/Jump__007.png'),(71,90)),
        pygame.transform.scale(pygame.image.load('images/png/Jump__008.png'),(71,90)),
        pygame.transform.scale(pygame.image.load('images/png/Jump__009.png'),(71,90)),
                ]
player2Stand = pygame.image.load("images/png2/Idle__000.png")

player2_rect = player2Stand.get_rect()
bg = pygame.transform.scale(pygame.image.load('images/Battleground1.jpg'),(800,600))
go = pygame.transform.scale(pygame.image.load('images/GameOver.jpg'),(800,600))
