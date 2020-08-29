from setup.definitions import *
from setup.settings import *


class Player(object):
    def __init__(self, isPlayer=True):
        self.isPlayer = isPlayer
        self.score = 0
        self.speed = -5
        self.frames = 0
        self.createPaddle()

    def createPaddle(self):
        if (self.isPlayer):
            self.paddle = Paddle(
                BORDERS[1],
                BORDERS[2] -
                Paddle().height)  # Starting Player location
        if (not self.isPlayer):
            # Starting computer location
            self.paddle = Paddle(BORDERS[0], BORDERS[3])

    def displayPaddle(self):
        self.paddle.displaySelf()

    def checkWin(self):
        if (self.score >= 7):
            return True
        else:
            return False

    def checkHitbox(self, ball):
        collision = self.paddle.checkHit(ball, self.isPlayer)
        return collision

    def movePaddle(self, ball):
        if (self.paddle.yPos <= 0) or (
                self.paddle.yPos + self.paddle.height >= DISPHEIGHT):
            self.paddle.yChange = 0
        elif (self.frames % 10 == 0):
            self.paddle.yChange = self.paddle.yChange * 0.95

        if ((ball.yPos - ball.height < self.paddle.yPos)
                and (self.paddle.yPos >= BORDERS[2])):
            self.paddle.yChange = self.speed + 2
        if ((ball.yPos > self.paddle.yPos + self.paddle.height)
                and (self.paddle.yPos + self.paddle.height <= BORDERS[3])):
            self.paddle.yChange = -(self.speed) - 2
