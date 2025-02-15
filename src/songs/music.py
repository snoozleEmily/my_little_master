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

    @staticmethod
    def start_music(path):
        if path.mp3_files:
            print(f"Playing: {path.mp3_files[0]}")
            pygame.mixer.music.load(path.mp3_files[0])
            pygame.mixer.music.set_volume(0.5)  # Adjust volume
            pygame.mixer.music.play()

    @staticmethod
    def check_current_music(path):
        if path.mp3_files and not pygame.mixer.music.get_busy():
            # Save the current song as the previous song
            if path.previous_song is not None:
                path.previous_song = path.mp3_files[0]

            # Move the current song to the end of the playlist
            next_song = path.mp3_files.pop(0)
            path.mp3_files.append(next_song)

            print(f"Playing next song: {path.mp3_files[0]}")
            pygame.mixer.music.load(path.mp3_files[0])
            pygame.mixer.music.play()
