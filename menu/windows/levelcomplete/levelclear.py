import pygame
import os
from util.screens import Screens
from util.prepare import SURF, WINDOW
from util.update_screen import update_screen
from util.screenshot import save_screenshot

def load_levelclear_image():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, "levelclear.png")
    return pygame.image.load(image_path)

def load_levelclear_background():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, "..", "40opacitybackround.png")
    return pygame.image.load(image_path)

async def levelclear() -> Screens:
    save_screenshot(SURF, "levelclear")
    
    levelclear_image = load_levelclear_image()
    background = load_levelclear_background()
    
    image_rect = levelclear_image.get_rect()
    image_rect.center = (WINDOW[0] // 2, WINDOW[1] // 2)
    
    background_rect = background.get_rect()
    background_rect.center = (WINDOW[0] // 2, WINDOW[1] // 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return Screens.MENU
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    return Screens.MENU
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    return Screens.MENU
        
        SURF.blit(background, background_rect)
        SURF.blit(levelclear_image, image_rect)
        
        await update_screen()
