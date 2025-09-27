import pygame
import pygame_gui
from util.screens import Screens
<<<<<<< Updated upstream
# from menu.menu import menu
from util.prepare import WINDOW #, CLOCK
from .theme import gamethemes
from .background import loadthebackround, blackoverlay
from util.update_screen import update_screen
from .elements import button_configs, label_configs
from util.prepare import FPS

async def menu() -> Screens:
    manager = pygame_gui.UIManager(WINDOW, gamethemes())
    background = loadthebackround()
    button_config = button_configs()
    label_config = label_configs()
=======
from util.prepare import WINDOW #, clock
from .theme import gametheme
from .background import loadthebackround, blackoverlay as create_overlay 
from util.update_screen import update_screen
from .elements import button_configs, label_configs as get_label_config
from util.prepare import FPS

async def menu() -> Screens:
    manager = pygame_gui.UIManager(WINDOW, gametheme())
    background = loadthebackround()
    button_config = button_configs()
    label_config = get_label_config()
>>>>>>> Stashed changes
    
    title_text = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect(*label_config["title"]["rect"]),
        text=label_config["title"]["text"],
        manager=manager
    )
    
    subtitle_text = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect(*label_config["subtitle"]["rect"]),
        text=label_config["subtitle"]["text"],
        manager=manager
    )
    
    play_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(*button_config["play"]["rect"]),
        text=button_config["play"]["text"],
        manager=manager
    )
    
    settings_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(*button_config["settings"]["rect"]),
        text=button_config["settings"]["text"],
        manager=manager
    )
    
    quit_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect(*button_config["quit"]["rect"]),
        text=button_config["quit"]["text"],
        manager=manager
    )
    
    while True:
<<<<<<< Updated upstream
        time_delta = await update_screen()
=======
        time_delta = 1/FPS
>>>>>>> Stashed changes
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return Screens.MENU
            
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == play_button:
                    return Screens.GAME
                elif event.ui_element == settings_button:
                    pass
                elif event.ui_element == quit_button:
<<<<<<< Updated upstream
                    raise SystemExit
=======
                    return Screens.MENU
>>>>>>> Stashed changes
            
            manager.process_events(event)
        
        manager.update(time_delta)
        
        screen = pygame.display.get_surface()
        screen.blit(background, (0, 0))
<<<<<<< Updated upstream
        overlay = blackoverlay()
        screen.blit(overlay, (0, 0))
        manager.draw_ui(screen)
=======
        overlay = create_overlay()
        screen.blit(overlay, (0, 0))
        manager.draw_ui(screen)
        update_screen()
>>>>>>> Stashed changes
