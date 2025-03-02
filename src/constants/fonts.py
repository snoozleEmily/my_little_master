import os
import pygame

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "..", "..", "..", "data", "assets", "fonts")

FONT_DEFAULT = pygame.font.Font(
    os.path.join(BASE_DIR, "fonts"), 28  # Baby Doll
)
FONT_CURSIVE = pygame.font.Font(
    os.path.join(BASE_DIR, "fonts"), 36  # Skeetch
)
FONT_BUTTON = pygame.font.SysFont("Roboto", 36)  # Roboto


# I got this fonts from my other game, 
# they are only placehodlers. We can definitely change them!!!