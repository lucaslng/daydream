import pygame
import os
import time
from util.screens import Screens
from util.prepare import SURF, WINDOW
from util.update_screen import update_screen

def load_finalsummary_background():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, "..", "40opacitybackround.png")
    return pygame.image.load(image_path)

async def finalsummary(level_system) -> Screens:
    background = load_finalsummary_background()
    background_rect = background.get_rect()
    background_rect.center = (WINDOW[0] // 2, WINDOW[1] // 2)
    
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        font_path = os.path.join(script_dir, "menu", "resources", "fonts", "LowresPixel-Regular.otf")
        font = pygame.font.Font(font_path, 24)
        small_font = pygame.font.Font(font_path, 18)
    except:
        font = pygame.font.SysFont("arial", 24, bold=True)
        small_font = pygame.font.SysFont("arial", 18, bold=True)
    
    def format_time(seconds: float) -> str:
        minutes = int(seconds // 60)
        seconds = seconds % 60
        return f"{minutes}:{seconds:05.2f}"
    
    def draw_shadow_text(text: str, x: int, y: int, font_obj, color=(255, 255, 255)):
        shadow = font_obj.render(text, True, (0, 0, 0))
        main = font_obj.render(text, True, color)
        SURF.blit(shadow, (x + 2, y + 2))
        SURF.blit(main, (x, y))
    
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
        
        center_x = WINDOW[0] // 2
        start_y = WINDOW[1] // 2 - 100
        
        draw_shadow_text("FINAL TIMES", center_x - 100, start_y, font, (255, 255, 0))
        
        y_offset = start_y + 60
        for i, level_time in enumerate(level_system.level_times):
            if level_time > 0:
                draw_shadow_text(f"Level {i+1}: {format_time(level_time)}", center_x - 80, y_offset, small_font)
                y_offset += 35
        
        total_time = level_system.get_total_time()
        draw_shadow_text(f"TOTAL: {format_time(total_time)}", center_x - 60, y_offset + 20, font, (0, 255, 0))
        
        draw_shadow_text("Click or press any key to continue", center_x - 120, y_offset + 80, small_font, (200, 200, 200))
        
        await update_screen()
