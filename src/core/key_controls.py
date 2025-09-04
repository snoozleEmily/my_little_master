import pygame



class KeyControls:
    def __init__(self, display, music_controller):
        self.display = display
        self.music_controller = music_controller
        self.running = True
        self.event_handlers = {
            pygame.QUIT: self.handle_quit,
            pygame.VIDEORESIZE: self.handle_resize,
            pygame.KEYDOWN: self.handle_keydown
        }

    def process_events(self):
        for event in pygame.event.get():
            if event.type in self.event_handlers:
                self.event_handlers[event.type](event)

    def handle_quit(self, event):
        self.running = False

    def handle_resize(self, event):
        self.display.handle_resize(event)

    def handle_keydown(self, event):
        if event.key == pygame.K_F1:
            self.display.toggle_fullscreen()
        elif event.key == pygame.K_ESCAPE:
            if self.display.fullscreen:  
                self.display.toggle_fullscreen()