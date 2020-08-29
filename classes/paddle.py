from setup.definitions import *
from setup.settings import *


class Paddle(object):
    def __init__(self, x=0, y=0):
        self.width = 10
        self.height = 90
        self.xPos = x
        self.yPos = y
        self.pos = (self.xPos, self.yPos)
        self.yChange = 0
        self.img = pygame.image.load('img/paddle.png')

    def checkHit(self, ball, isPlayer):
        collision = False
        self.xRange = range(int(self.xPos), int(self.xPos) + self.width)
        self.yRange = range(int(self.yPos), int(self.yPos) + self.height)
        ballyRange = range(int(ball.yPos), int(ball.yPos) + ball.height)
        ballxRange = range(int(ball.xPos), int(ball.xPos) + ball.width)

        if ((ballyRange[0] in self.yRange) or (ballyRange[-1] in self.yRange)):
            if ((ballxRange[0] in self.xRange) or (
                    ballxRange[-1] in self.xRange)):
                collision = True

        return collision

    def updatePos(self):
        self.yPos += self.yChange
        self.pos = (self.xPos, self.yPos)

    def displaySelf(self):
        self.updatePos()
        gameDisplay.blit(self.img, self.pos)
