import pygame
import os
from util.prepare import WINDOW


def loadthebackround():
    try:
        # Get the directory of this script and construct the path
        script_dir = os.path.dirname(os.path.abspath(__file__))
        background_path = os.path.join(script_dir, "elements", "menubackround.png")
        background = pygame.image.load(background_path)
        background = pygame.transform.scale(background, WINDOW)
        return background
    except pygame.error: # fallback to a black screen
        background = pygame.Surface(WINDOW)
        background.fill((0, 0, 0))
        return background


def blackoverlay():
    overlay = pygame.Surface(WINDOW)
    overlay.set_alpha(100)
    overlay.fill((0, 0, 0)) 
    return overlay
