import pygame
import sys
import random

'''
Initializes pygame to run.
This function must be called before
any other pygame functions/methods can be used.
'''

pygame.init()

global FPS, DISPWIDTH, DISPHEIGHT, PADDING, BORDERS, COLORS
global gameDisplay, clock

# constant values
FPS = 65
DISPWIDTH = 800
DISPHEIGHT = 600
PADDING = (DISPWIDTH / 32, DISPHEIGHT / 6)
BORDERS = (
    PADDING[0],
    DISPWIDTH -
    PADDING[0],
    PADDING[1],
    DISPHEIGHT -
    PADDING[1])  # (x1,x2,y1,y2)
COLORS = {
    'BLACK': (0, 0, 0, 0),
    'WHITE': (255, 255, 255),
    'RED': (255, 0, 0),
    'GREEN': (7, 99, 36),
    'BLUE': (0, 0, 255)
}

# objects
gameDisplay = pygame.display.set_mode((DISPWIDTH, DISPHEIGHT))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()

# pygame functions


def quitGame():
    '''
    Performs the function of quitting the game
    '''
    pygame.quit()
    sys.exit()


def checkQuit(event):
    '''
    Checks to see if the user clicked the X button on the window
    '''
    if event.type == pygame.QUIT:
        quitGame()


def displayText(text, size, xyPos, textColor, bgColor):
    '''
    Takes in a string, size int, xy tuple, and colors as arguments,
    and displays the given string with the given size to the given location
    '''
    font = pygame.font.Font("freesansbold.ttf", size)
    nText = font.render(text, True, textColor, bgColor)
    gameDisplay.blit(nText, xyPos)


def updateScreen(delay=0):
    '''
    Uodates the screen with the constant FPS value
    '''
    pygame.display.update()
    clock.tick(FPS)
    pygame.time.delay(delay)
