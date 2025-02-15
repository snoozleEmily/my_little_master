import pygame

from songs.music import SongsPath
from constants.colors import BACKGROUND_COLOR
from constants.project_config import WIDTH, HEIGHT

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("My Little Master")

songs_path: SongsPath = SongsPath()
SongsPath.start_music(songs_path)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

    # Check and play next song if the current one finishes
    SongsPath.check_current_music(songs_path)

    # Fill background
    screen.fill(BACKGROUND_COLOR)

    # Update display
    pygame.display.flip()

# Quit pygame
pygame.quit()
