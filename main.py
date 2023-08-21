import os
import pygame
import tkinter as tk
from tkinter import filedialog


class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")

        self.music_folder = ""
        self.playlist = []
        self.current_track_index = 0

        self.create_buttons()
        self.load_music_folder()

    def create_buttons(self):
        button_texts = ["Load Music Folder", "Play", "Next Track", "Previous Track", "Stop"]
        button_commands = [self.load_music_folder, self.play, self.next_track, self.previous_track, self.stop]

        for text, command in zip(button_texts, button_commands):
            button = tk.Button(self.root, text=text, command=command, font=("Helvetica", 14))
            button.pack(pady=8)

    def load_music_folder(self):
        self.music_folder = filedialog.askdirectory()
        self.playlist = [f for f in os.listdir(self.music_folder) if f.endswith(".mp3")]

    def play(self):
        if not self.playlist:
            print("No music files found in the playlist.")
            return

        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(self.music_folder, self.playlist[self.current_track_index]))
        pygame.mixer.music.play()

    def next_track(self):
        if self.current_track_index < len(self.playlist) - 1:
            self.current_track_index += 1
            self.play()

    def previous_track(self):
        if self.current_track_index > 0:
            self.current_track_index -= 1
            self.play()

    def stop(self):
        pygame.mixer.music.stop()


if __name__ == "__main__":
    pygame.mixer.init()
    root = tk.Tk()
    root.title("Music Player")

    # Set window size and position
    window_width = 500
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Disable maximize button
    root.resizable(width=False, height=False)

    # Set black background
    root.configure(bg="black")

    player = MusicPlayer(root)

    root.mainloop()
    pygame.mixer.quit()
import os
import pygame
import tkinter as tk
from tkinter import filedialog


class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")

        self.music_folder = ""
        self.playlist = []
        self.current_track_index = 0

        self.create_buttons()
        self.load_music_folder()

    def create_buttons(self):
        button_texts = ["Load Music Folder", "Play", "Next Track", "Previous Track", "Stop"]
        button_commands = [self.load_music_folder, self.play, self.next_track, self.previous_track, self.stop]

        for text, command in zip(button_texts, button_commands):
            button = tk.Button(self.root, text=text, command=command, font=("Helvetica", 14))
            button.pack(pady=8)

    def load_music_folder(self):
        self.music_folder = filedialog.askdirectory()
        self.playlist = [f for f in os.listdir(self.music_folder) if f.endswith(".mp3")]

    def play(self):
        if not self.playlist:
            print("No music files found in the playlist.")
            return

        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(self.music_folder, self.playlist[self.current_track_index]))
        pygame.mixer.music.play()

    def next_track(self):
        if self.current_track_index < len(self.playlist) - 1:
            self.current_track_index += 1
            self.play()

    def previous_track(self):
        if self.current_track_index > 0:
            self.current_track_index -= 1
            self.play()

    def stop(self):
        pygame.mixer.music.stop()


if __name__ == "__main__":
    pygame.mixer.init()
    root = tk.Tk()
    root.title("Music Player")

    # Set window size and position
    window_width = 500
    window_height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Disable maximize button
    root.resizable(width=False, height=False)

    # Set black background
    root.configure(bg="black")

    player = MusicPlayer(root)

    root.mainloop()
    pygame.mixer.quit()
