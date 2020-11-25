class players:
     def __init__(self, x ,y ,width ,height,leftImage,rightImage,playerStand,number):
         self.x = x
         self.y = y
         self.width = width
         self.height = height
         self.walkRight = rightImage
         self.walkLeft = leftImage
         self.playerStand = playerStand
         self.speed = 1
         self.jump = False
         self.jumpCount = 0
         self.left = False
         self.right = False
         self.animCount = 0
         self.number = number
         
class lifes:
     def __init__(self, x, width, number):
         self.x = x
         self.y = 10
         self.width = width
         self.height = 20
         self.number = number

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

