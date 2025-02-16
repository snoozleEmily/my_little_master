import pygame

from core.display_manager import DisplayManager
from core.key_controls import KeyControls
from core.sound_controller import SoundController
from constants.colors import BACKGROUND_COLOR
from constants.project_config import WIDTH, HEIGHT

def main():
    pygame.init()
    pygame.mixer.init()

    display = DisplayManager(WIDTH, HEIGHT)
    music_controller = SoundController()
    event_handler = KeyControls(display, music_controller)

    music_controller.start_music()

    while event_handler.running:
        event_handler.process_events()
        music_controller.check_music()
        
        display.screen.fill(BACKGROUND_COLOR)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()