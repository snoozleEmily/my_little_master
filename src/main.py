import pygame

from core.display_manager import DisplayManager
from core.signal_monitor import SignalMonitor
from core.sound_controller import SoundController
from constants.colors import BACKGROUND_COLOR
from constants.project_config import WIDTH, HEIGHT

def main():
    pygame.init()
    pygame.mixer.init()

    display = DisplayManager(WIDTH, HEIGHT)
    music_controller = SoundController()
    event_handler = SignalMonitor(display, music_controller)

    music_controller.start_music()

    while event_handler.running:
        event_handler.process_events()
        music_controller.check_music_status()
        
        display.screen.fill(BACKGROUND_COLOR)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()