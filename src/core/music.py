import os
import pygame

from constants.project_config import BASE_DIR


pygame.mixer.init()

PLAYLIST_DIR = os.path.join(BASE_DIR, "..", "..", "data", "assets", "music")


class SongsPath:
    def __init__(self):
        self.mp3_files = [
            os.path.join(PLAYLIST_DIR, file)
            for file in os.listdir(PLAYLIST_DIR)
            if file.endswith(".mp3")
        ]
        self.previous_song = None
        print("MP3 Files:", self.mp3_files)  # Debugging

    def start_music(self):
        if self.mp3_files:
            print(f"Playing: {self.mp3_files[0]}")
            pygame.mixer.music.load(self.mp3_files[0])
            pygame.mixer.music.set_volume(0.5)  # Adjust volume
            pygame.mixer.music.play()
            
    def check_music(self):
        if self.mp3_files and not pygame.mixer.music.get_busy():
            # Save the current song as the previous song
            if self.previous_song is not None:
                self.previous_song = self.mp3_files[0]

            # Move the current song to the end of the playlist
            next_song = self.mp3_files.pop(0)
            self.mp3_files.append(next_song)

            print(f"Playing next song: {self.mp3_files[0]}")
            pygame.mixer.music.load(self.mp3_files[0])
            pygame.mixer.music.play()
