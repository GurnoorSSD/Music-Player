import pygame
import tkinter as tk
from tkinter import filedialog

# Initialize Pygame mixer
pygame.mixer.init()

# Create main window
root = tk.Tk()
root.title("Simple Music Player")
root.geometry("300x200")

# Load a music file
def load_music():
    music_file = filedialog.askopenfilename(
        title="Select a music file",
        filetypes=(("MP3 Files", "*.mp3"), ("All Files", "*.*"))
    )
    if music_file:
        pygame.mixer.music.load(music_file)
        song_label.config(text=f"Loaded: {music_file.split('/')[-1]}")

# Play music
def play_music():
    pygame.mixer.music.play()

# Pause music
def pause_music():
    pygame.mixer.music.pause()

# Resume music
def resume_music():
    pygame.mixer.music.unpause()

# Stop music
def stop_music():
    pygame.mixer.music.stop()

# UI Buttons
tk.Button(root, text="Load", command=load_music).pack(pady=5)
tk.Button(root, text="Play", command=play_music).pack(pady=5)
tk.Button(root, text="Pause", command=pause_music).pack(pady=5)
tk.Button(root, text="Resume", command=resume_music).pack(pady=5)
tk.Button(root, text="Stop", command=stop_music).pack(pady=5)

song_label = tk.Label(root, text="No song loaded")
song_label.pack(pady=10)

root.mainloop()
