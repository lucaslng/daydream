import pygame
import os
from util.screens import Screens
from util.prepare import SURF, WINDOW
from util.update_screen import update_screen

def load_ingamemenu_image():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, "40opacitybackround.png")
    return pygame.image.load(image_path)

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

async def ingamemenu(hud_system=None) -> Screens:
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        font_path = os.path.join(script_dir, "..", "..", "..", "menu", "resources", "fonts", "LowresPixel-Regular.otf")
        button_font = pygame.font.Font(font_path, 22)
    except:
        button_font = pygame.font.SysFont("arial", 22, bold=True)
    
    button_width = 160
    button_height = 35
    center_x = WINDOW[0] // 2
    center_y = WINDOW[1] // 2
    
    resume_rect = pygame.Rect(center_x - button_width//2, center_y - 20, button_width, button_height)
    quit_rect = pygame.Rect(center_x - button_width//2, center_y + 25, button_width, button_height)
    
    # Pause timer when menu opens
    if hud_system:
        hud_system.pause_timer()
    
    while True:
        mouse_pos = pygame.mouse.get_pos()
        
        resume_hovered = resume_rect.collidepoint(mouse_pos)
        quit_hovered = quit_rect.collidepoint(mouse_pos)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return Screens.MENU
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if hud_system:
                        hud_system.resume_timer()
                    return Screens.GAME
                if event.key == pygame.K_RETURN:
                    if hud_system:
                        hud_system.resume_timer()
                    return Screens.GAME
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if resume_hovered:
                        if hud_system:
                            hud_system.resume_timer()
                        return Screens.GAME
                    elif quit_hovered:
                        if hud_system:
                            hud_system.resume_timer()
                        return Screens.MENU
        
        draw_button(SURF, resume_rect, "Resume", button_font, (255, 255, 255), resume_hovered)
        draw_button(SURF, quit_rect, "Quit", button_font, (255, 255, 255), quit_hovered)
        
        await update_screen()
