import pygame
import os
from util.screens import Screens
from util.prepare import SURF, WINDOW #, clock
from .theme import gametheme
from .background import loadthebackround, blackoverlay as create_overlay 
from util.update_screen import update_screen
from .elements import button_configs, label_configs as get_label_config

def draw_shadow_text(screen, font, text, x, y, color=(255,255,255)):
    shadow = font.render(text, True, (0,0,0))
    main = font.render(text, True, color)
    screen.blit(shadow, (x+2, y+2))
    screen.blit(main, (x, y))

def draw_button(screen, rect, text, font, color, is_hovered):
    if is_hovered:
        color = (255, 215, 0)
    
    text_surf = font.render(text, True, color)
    text_rect = text_surf.get_rect()
    text_rect.center = rect.center
    
    shadow = font.render(text, True, (0,0,0))
    screen.blit(shadow, (text_rect.x+2, text_rect.y+2))
    screen.blit(text_surf, text_rect)

async def menu() -> Screens:
    background = loadthebackround()
    button_config = button_configs()
    label_config = get_label_config()
    
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        font_path = os.path.join(script_dir, "resources", "fonts", "LowresPixel-Regular.otf")
        title_font = pygame.font.Font(font_path, 28)
        button_font = pygame.font.Font(font_path, 22)
    except:
        title_font = pygame.font.SysFont("arial", 28, bold=True)
        button_font = pygame.font.SysFont("arial", 22, bold=True)
    
    play_rect = pygame.Rect(*button_config["play"]["rect"])
    settings_rect = pygame.Rect(*button_config["settings"]["rect"])
    quit_rect = pygame.Rect(*button_config["quit"]["rect"])
    
    while True:
        mouse_pos = pygame.mouse.get_pos()
        
        play_hovered = play_rect.collidepoint(mouse_pos)
        settings_hovered = settings_rect.collidepoint(mouse_pos)
        quit_hovered = quit_rect.collidepoint(mouse_pos)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return Screens.MENU
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if play_hovered:
                        return Screens.GAME
                    elif settings_hovered:
                        pass
                    elif quit_hovered:
                        raise SystemExit
        
        manager.update(time_delta)
        
        SURF.blit(background, (0, 0))
        overlay = create_overlay()
        SURF.blit(overlay, (0, 0))
        manager.draw_ui(SURF)
        await update_screen()
