from setup.definitions import *
from setup.settings import *


class Ball(object):
    def __init__(self):
        self.width = 10
        self.height = 15
        self.xPos = DISPWIDTH / 2
        self.yPos = DISPHEIGHT / 2
        self.pos = (self.xPos, self.yPos)
        self.speed = 6
        self.xChange = self.speed - random.uniform(0, 2)
        self.yChange = 0
        self.img = pygame.image.load('img/ball.png')

    def resetPos(self):
        self.xPos = DISPWIDTH / 2
        self.yPos = DISPHEIGHT / 2
        self.xChange = self.speed - random.uniform(0, 2)
        self.yChange = 0

    def getPosChange(self, paddle, isPlayer):
        if isPlayer:
            self.xChange = -(self.speed)
        else:
            self.xChange = (self.speed)

        distFromMid = (paddle.pos[1] + (paddle.height / 2)) - self.pos[1]
        # Represents the slope of a linear graph
        changeInSpeed = self.speed / (paddle.height / 2)
        self.yChange = -(distFromMid * changeInSpeed)

    def updatePos(self):
        self.xPos += self.xChange
        self.yPos += self.yChange
        self.pos = (self.xPos, self.yPos)

    def displaySelf(self):
        self.updatePos()
        gameDisplay.blit(self.img, self.pos)
