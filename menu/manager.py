import pygame


class managerr:
    def __init__(self):
        self.current_screen = "main"
        self.selected_option = None
        self.clock = pygame.time.Clock()
        

    def switch_screen(self, screen_name):
        self.current_screen = screen_name

    def select_option(self, option):
        self.selected_option = option

    def get_state(self):
        return {
            "screen": self.current_screen,
            "selected": self.selected_option
        }
    
    def update(self, time_delta):
        pass
    
    def draw_ui(self, screen):
        pass