import pygame



from core.key_controls import KeyControls
from core.display_manager import DisplayManager
from core.sound_controller import SoundController
from constants.project_config import WIDTH, HEIGHT




def main():
    pygame.init()
    pygame.mixer.init()

    display = DisplayManager(WIDTH, HEIGHT)
    music = SoundController()
    controls = KeyControls(display, music)

    music.start_music()

    while controls.running:
        controls.process_events()
        music.check_music()

        # To add more elements to the screen, handle them on a separate file
        # the main loop should have the minimun amount of code possible 
        # for better readability and maintainance
        
        display.update_screen()

    pygame.quit()

if __name__ == "__main__":
    main()