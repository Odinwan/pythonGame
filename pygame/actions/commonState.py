def checkPosition(player1,player2):
    if (player1.rect.x >= player2.rect.x):
        player1.position = 'left'
        player2.position = 'right'
    else:
        player2.position = 'left'
        player1.position = 'right'
