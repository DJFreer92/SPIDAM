from view import View
from model import Model
from tkinter import filedialog as fd


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.audio_file = ''
    #the specific files that can be chosen to analyze
    def select_audio_file(self):
        filetypes = (
            ('audio files', ('*.wav','*.mp3')),
            ('mp3 files', '*.mp3*'),
            ('wav files', '*.wav')
        )

        self.audio_file = fd.askopenfilename(
            title = 'Open a file',
            initialdir = '/',
            filetypes = filetypes
        )

        if self.audio_file:
            self.model.set_file_path(self.audio_file)
