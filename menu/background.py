import pygame
import os
from util.prepare import SURF, WINDOW


def loadthebackround():
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        background_path = os.path.join(script_dir, "elements", "menubackround.png")
        background = pygame.image.load(background_path)
        background = pygame.transform.scale(background, WINDOW)
        return background
    except pygame.error:
        background = pygame.Surface(WINDOW)
        background.fill((0, 0, 0))
        return background


def blackoverlay():
    overlay = pygame.Surface(WINDOW)
    overlay.set_alpha(100)
    overlay.fill((0, 0, 0)) 
    return overlay
