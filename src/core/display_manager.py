import pygame

class DisplayManager:
    """Class to manage the screen of the game."""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.fullscreen = False
        self.screen = pygame.display.set_mode(
            (self.width, self.height), 
            pygame.RESIZABLE
        )
        
    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        if self.fullscreen:
            info = pygame.display.Info()
            self.screen = pygame.display.set_mode(
                (info.current_w, info.current_h),
                pygame.FULLSCREEN
            )
        else:
            self.screen = pygame.display.set_mode(
                (self.width, self.height),
                pygame.RESIZABLE
            )
    
    def handle_resize(self, event):
        if not self.fullscreen:
            self.width, self.height = event.w, event.h
            self.screen = pygame.display.set_mode(
                (self.width, self.height),
                pygame.RESIZABLE
            )