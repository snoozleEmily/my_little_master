# core/text.py
import pygame

class Text:
    def __init__(self, display, message, x, y, font_size=36, color=(255, 255, 255)):
        """
        Simple text rendering class.

        Args:
            display (DisplayManager): Your DisplayManager instance.
            message (str): Text message to display.
            x (int): X position.
            y (int): Y position.
            font_size (int): Font size.
            color (tuple): RGB color (default: white).
        """
        self.display = display
        self.message = message
        self.x = x
        self.y = y
        self.font_size = font_size
        self.color = color
        self.font = pygame.font.Font(None, self.font_size)

    def draw(self):
        """Render the text onto the display surface."""
        text_surface = self.font.render(self.message, True, self.color)
        self.display.screen.blit(text_surface, (self.x, self.y))