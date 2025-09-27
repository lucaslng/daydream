import pygame
from util.prepare import WINDOW

def loadthebackround():
    try:
        background = pygame.image.load("menu/resources/main-backround.png") # tbd to change path
        background = pygame.transform.scale(background, WINDOW)
        return background
    except pygame.error: #fallback to black screen
        background = pygame.Surface(WINDOW)
        background.fill((0, 0, 0))
        return background


def blackoverlay():
    overlay = pygame.Surface(WINDOW)
    overlay.set_alpha(100)
    overlay.fill((0, 0, 0)) 
    return overlay
