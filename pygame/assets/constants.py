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
go = pygame.transform.scale(pygame.image.load('images/GameOver.jpg'),(800,600))

firstWalk = [pygame.image.load('images/png/Run__000.png'),
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

firstAttack = [pygame.transform.scale(pygame.image.load('images/png/Attack__000.png'),(90,100)),
                pygame.transform.scale(pygame.image.load('images/png/Attack__001.png'),(90,100)),
                pygame.transform.scale(pygame.image.load('images/png/Attack__002.png'),(90,100)),
                pygame.transform.scale(pygame.image.load('images/png/Attack__003.png'),(90,100)),
                pygame.transform.scale(pygame.image.load('images/png/Attack__004.png'),(90,100)),
                pygame.transform.scale(pygame.image.load('images/png/Attack__005.png'),(90,100)),
                pygame.transform.scale(pygame.image.load('images/png/Attack__006.png'),(90,100)),
                pygame.transform.scale(pygame.image.load('images/png/Attack__007.png'),(90,100)),
                pygame.transform.scale(pygame.image.load('images/png/Attack__008.png'),(90,100)),
                pygame.transform.scale(pygame.image.load('images/png/Attack__009.png'),(90,100)),
                ]
firstJump = [pygame.transform.scale(pygame.image.load('images/png/Jump__000.png'),(71,90)),
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
firstStay = [pygame.transform.scale(pygame.image.load('images/png/Idle__000.png'),(52,90)),
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

secondWalk = [pygame.transform.scale(pygame.image.load('images/png2/Run__000.png'),(71,90)),
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

secondAttack = [pygame.transform.scale(pygame.image.load('images/png2/Attack__000.png'),(120,100)),
                pygame.transform.scale(pygame.image.load('images/png2/Attack__001.png'),(120,100)),
                pygame.transform.scale(pygame.image.load('images/png2/Attack__002.png'),(120,100)),
                pygame.transform.scale(pygame.image.load('images/png2/Attack__003.png'),(120,100)),
                pygame.transform.scale(pygame.image.load('images/png2/Attack__004.png'),(120,100)),
                pygame.transform.scale(pygame.image.load('images/png2/Attack__005.png'),(120,100)),
                pygame.transform.scale(pygame.image.load('images/png2/Attack__006.png'),(120,100)),
                pygame.transform.scale(pygame.image.load('images/png2/Attack__007.png'),(120,100)),
                pygame.transform.scale(pygame.image.load('images/png2/Attack__008.png'),(120,100)),
                pygame.transform.scale(pygame.image.load('images/png2/Attack__009.png'),(120,100)),
                ]
secondJump = [pygame.transform.scale(pygame.image.load('images/png2/Jump__000.png'),(71,90)),
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

secondStay = [pygame.transform.scale(pygame.image.load('images/png2/Idle__000.png'),(52,90)),
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

firstShock = pygame.transform.scale(pygame.image.load('images/png/Dead__000.png'),(100,110))
secondShock = pygame.transform.scale(pygame.image.load('images/png2/Dead__000.png'),(100,110))
bg = pygame.image.load("images/Battleground1.jpg")
