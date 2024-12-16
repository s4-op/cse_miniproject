import tkinter as tk
from tkinter import filedialog
import pygame

# Initialize pygame mixer
pygame.mixer.init()

class MusicPlayer:
    def _init_(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x200")
        
        self.load_button = tk.Button(self.root, text="Load Music", command=self.load_music)
        self.load_button.pack(pady=20)
        
        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack(pady=10)
        
        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_music)
        self.pause_button.pack(pady=10)
        
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=10)
        
        self.music_file = None
    
    def load_music(self):
        self.music_file = filedialog.askopenfilename(filetypes=[("Music Files", "*.mp3 *.wav")])
    
    def play_music(self):
        if self.music_file:
            pygame.mixer.music.load(self.music_file)
            pygame.mixer.music.play()
    
    def pause_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
    
    def stop_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()

# Create the Tkinter window
root = tk.Tk()
app = MusicPlayer(root)
root.mainloop()