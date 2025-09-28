import pygame
import os
import time
import asyncio
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

async def levelclear(level_system=None) -> Screens:
    save_screenshot(SURF, "levelclear")
    
    levelclear_image = load_levelclear_image()
    background = load_levelclear_background()
    
    image_rect = levelclear_image.get_rect()
    image_rect.center = (WINDOW[0] // 2, WINDOW[1] // 2)
    
    background_rect = background.get_rect()
    background_rect.center = (WINDOW[0] // 2, WINDOW[1] // 2)
    
    start_time = time.time()
    display_time = 3.0
    
    while True:
        current_time = time.time()
        elapsed = current_time - start_time
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return Screens.MENU
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    if level_system and not level_system.is_game_complete():
                        level_system.next_level()
                        return Screens.GAME
                    else:
                        return Screens.MENU
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if level_system and not level_system.is_game_complete():
                        level_system.next_level()
                        return Screens.GAME
                    else:
                        return Screens.MENU
        
        if elapsed >= display_time:
            if level_system and not level_system.is_game_complete():
                level_system.next_level()
                return Screens.GAME
            else:
                return Screens.MENU
        
        SURF.blit(background, background_rect)
        SURF.blit(levelclear_image, image_rect)
        
        await update_screen()
