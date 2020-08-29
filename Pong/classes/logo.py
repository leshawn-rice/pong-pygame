from setup.definitions import *
from setup.settings import *


class Logo(object):
    def __init__(self):
        self.width = 75
        self.height = 75
        self.xPos = DISPWIDTH / 2 - self.width / 3
        self.yPos = DISPHEIGHT / 2 - self.height / 3
        self.pos = (self.xPos, self.yPos)
        self.img = pygame.image.load("img/symbol.png")
        self.img = pygame.transform.scale(self.img, (self.height, self.width))

    def displaySelf(self):
        gameDisplay.blit(self.img, (self.xPos, self.yPos))
