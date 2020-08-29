from setup.settings import *
from classes.paddle import *
from classes.ball import *
from classes.player import *
from classes.logo import *
import game


def endGame(player):
    '''
    Acceots a user/computer player as the winner, uses player.isPlayer to determine outcome
    '''
    if (player.isPlayer):
        displayText("PLAYER WON", 50, (DISPWIDTH / 5, 50),
                    COLORS['WHITE'], COLORS['BLACK'])
        updateScreen(1000)
        menu(True)
    elif (not player.isPlayer):
        displayText("COMPUTER WON", 50, (DISPWIDTH / 5, 50),
                    COLORS['WHITE'], COLORS['BLACK'])
        updateScreen(1000)
        menu(True)
    else:
        print("Something strange happened!")
        quitGame()


def resetScreen(ball):
    ball.resetPos()
    for i in range(3):
        displayText(str(3-i), 100, (DISPWIDTH / 2 - 10, 50),
                COLORS['WHITE'], COLORS['BLACK'])
        updateScreen(1000)


def handleScore(player, ball):
    player.score += 1
    if (player.checkWin()):
        endGame(player)
    else:
        resetScreen(ball)


def checkPaddleCollision(user, computer, ball):
    '''Insert Comment'''
    userCollision = False
    computerCollision = False
    userCollision = user.checkHitbox(ball)
    computerCollision = computer.checkHitbox(ball)
    if (userCollision):
        ball.getPosChange(user.paddle, user.isPlayer)
    if (computerCollision):
        ball.getPosChange(computer.paddle, computer.isPlayer)

    if (user.paddle.yPos <= 0):  # If the paddle touches ceiling
        user.paddle.yChange = 0
    if (user.paddle.yPos + user.paddle.height >
            DISPHEIGHT):  # If the paddle touches floor
        user.paddle.yChange = 0


def checkBallCollision(user, computer, ball):
    '''Insert comment'''
    if (ball.xPos <= 0):  # If the ball passes the cpu paddle
        handleScore(user, ball)

    if (ball.xPos + ball.width >= DISPWIDTH):  # If the ball passes the player paddle
        handleScore(computer, ball)

    if (ball.yPos <= 0):  # If the ball touches the celing
        ball.yChange = 2
    if (ball.yPos + ball.height >= DISPHEIGHT):  # If the ball touches the floor
        ball.yChange = -2


def optionsMenu():
    inMenu = True
    while (inMenu):
        gameDisplay.fill(COLORS['BLACK'])
        displayText("OPTIONS", 100, (DISPWIDTH / 5, 50),
                    COLORS['WHITE'], COLORS['BLACK'])
        displayText("COMING SOON", 25, (DISPWIDTH / 5, 200),
                    COLORS['WHITE'], COLORS['BLACK'])
        displayText("GO BACK", 25, (DISPWIDTH / 5, 400),
                    COLORS['WHITE'], COLORS['BLACK'])
        updateScreen()
        for event in pygame.event.get():
            checkQuit(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if ((DISPWIDTH / 5 <= mouse[0] <= DISPWIDTH /
                     5 + 500) and (400 <= mouse[1] <= 500)):
                    return


def pauseMenu():
    paused = True
    while (paused):
        gameDisplay.fill(COLORS['BLACK'])
        displayText("PAUSED", 100, (DISPWIDTH / 4, 50),
                    COLORS['WHITE'], COLORS['BLACK'])
        displayText("OPTIONS", 100, (DISPWIDTH / 4, 250),
                    COLORS['WHITE'], COLORS['BLACK'])
        updateScreen()
        for event in pygame.event.get():
            checkQuit(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if ((DISPWIDTH / 4 <= mouse[0] <= DISPWIDTH /
                     4 + 500) and (250 <= mouse[1] <= 350)):
                    optionsMenu()


def menu(played=False):
    '''
    Displays the menu to the user
    '''
    inMenu = True
    while (inMenu):
        gameDisplay.fill(COLORS['BLACK'])
        buttonLocs = [(DISPWIDTH / 4, 50), (DISPWIDTH / 4, 250),
                      (DISPWIDTH / 4, 450)]
        displayText("PLAY", 100, buttonLocs[0],
                    COLORS['WHITE'], COLORS['BLACK'])
        displayText("OPTIONS", 100,
                    buttonLocs[1], COLORS['WHITE'], COLORS['BLACK'])
        displayText("QUIT", 100, buttonLocs[2],
                    COLORS['WHITE'], COLORS['BLACK'])
        updateScreen()

        for event in pygame.event.get():
            checkQuit(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if ((buttonLocs[0][0] <= mouse[0] <= buttonLocs[0][0] + 250)
                        and (buttonLocs[0][1] <= mouse[1] <= buttonLocs[0][1] + 100)):
                    if (not played):
                        return
                    else:
                        game.loop.gameLoop()
                if ((buttonLocs[1][0] <= mouse[0] <= buttonLocs[1][0] + 500)
                        and (buttonLocs[1][1] <= mouse[1] <= buttonLocs[1][1] + 100)):
                    optionsMenu()
                if ((buttonLocs[2][0] <= mouse[0] <= buttonLocs[2][0] + 250)
                        and (buttonLocs[2][1] <= mouse[1] <= buttonLocs[2][1] + 100)):
                    quitGame()
