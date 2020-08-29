from setup.settings import *
from setup.definitions import *


def fillScreen(user, computer, ball, logo):
    '''
    Fills the screen with the given color, displays objects
    '''
    scoreText = f"Player: {user.score}|Computer: {computer.score}"
    gameDisplay.fill(COLORS['BLACK'])
    displayText(scoreText, 50, (DISPWIDTH / 5, 550),
                COLORS['WHITE'], COLORS['BLACK'])
    user.displayPaddle()
    computer.displayPaddle()
    logo.displaySelf()
    ball.displaySelf()


def handleKeys(user, event):
    if event.key == pygame.K_UP:
        user.paddle.yChange = user.speed  # The paddle will travel up
    if event.key == pygame.K_DOWN:
        user.paddle.yChange = -(user.speed)  # The paddle will travel down
    if event.key == pygame.K_ESCAPE:
        pauseMenu()


def gameLoop():
    logo = Logo()
    ball = Ball()
    user = Player()
    computer = Player(False)

    playing = True

    fillScreen(user, computer, ball, logo)
    resetScreen(ball)

    while playing:

        fillScreen(user, computer, ball, logo)
        computer.frames += 1
        computer.movePaddle(ball)
        checkPaddleCollision(user, computer, ball)
        checkBallCollision(user, computer, ball)

        for event in pygame.event.get():
            checkQuit(event)
            if event.type == pygame.KEYDOWN:
                handleKeys(user, event)

        updateScreen()
