import pygame
from util.prepare import WINDOW


def load_game_background():
    background = pygame.Surface(WINDOW)
    background.fill((50, 50, 50))
    return background


def create_game_overlay():
    overlay = pygame.Surface(WINDOW)
    overlay.fill((0, 0, 0))
    overlay.set_alpha(102)
    return overlay
