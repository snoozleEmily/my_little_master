import pygame

from .music import SongsPath


class SoundController(SongsPath):
    """
    Gives functionality to sound-related settings buttons.
    """

    def __init__(self):
        super().__init__()
        self.volume = 0.3  # Default volume
        self.prev_volume = self.volume
        self.playing = True
        self.previous_song = None

    def toggle_mute(self):
        if self.playing:
            # Save the current volume
            self.prev_volume = self.volume
            pygame.mixer.music.set_volume(0)
        else:
            # Restore previous volume
            pygame.mixer.music.set_volume(self.prev_volume)
        self.playing = not self.playing

    def increase_volume(self):
        if self.volume < 1.0:
            self.volume += 0.1
            pygame.mixer.music.set_volume(self.volume)

    def decrease_volume(self):
        if self.volume > 0.0:
            self.volume -= 0.1
            pygame.mixer.music.set_volume(self.volume)

    def next_song(self):
        if self.playing and self.mp3_files:
            # Save the current song as the previous song
            self.previous_song = self.mp3_files[0]

            # Move the current song to the end of the playlist
            next_song = self.mp3_files.pop(0)
            self.mp3_files.append(next_song)

            # Stop the current song, it automatically plays the next one
            pygame.mixer.music.stop()

    def last_song(self):
        if self.previous_song:
            # Load and play the previous song
            pygame.mixer.music.load(self.previous_song)
            pygame.mixer.music.play()
