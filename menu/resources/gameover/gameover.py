import pygame
import os
from util.screens import Screens
from util.prepare import SURF, WINDOW
from util.update_screen import update_screen

def load_gameover_image():
    """Load the game over PNG image"""
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "gameover.png")
        return pygame.image.load(image_path)
    except pygame.error as e:
        print(f"Error loading gameover image: {e}")
        # Create a fallback surface if image fails to load
        fallback = pygame.Surface((400, 200))
        fallback.fill((255, 0, 0))  # Red fallback
        return fallback

def create_semi_transparent_overlay(alpha=64):
    """Create a semi-transparent overlay (25% opacity = 64/255)"""
    overlay = pygame.Surface(WINDOW)
    overlay.fill((0, 0, 0))  # Black background
    overlay.set_alpha(alpha)  # 25% opacity
    return overlay

async def gameover() -> Screens:
    """Game over screen with semi-transparent background"""
    gameover_image = load_gameover_image()
    
    # Center the game over image
    image_rect = gameover_image.get_rect()
    image_rect.center = (WINDOW[0] // 2, WINDOW[1] // 2)
    
    # Create semi-transparent overlay (25% opacity)
    overlay = create_semi_transparent_overlay(64)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return Screens.MENU
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    return Screens.MENU
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    return Screens.MENU
        
        # Draw the semi-transparent overlay first
        SURF.blit(overlay, (0, 0))
        
        # Draw the game over image on top
        SURF.blit(gameover_image, image_rect)
        
        await update_screen()
