from view import View
from model import Model
from tkinter import filedialog as fd


#Controller is to be written last
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.audio_file = ''

    #def Start():

    def select_audio_file(self):
        filetypes = (
            ('wav files', '*.wav'),
            ('mp3 files', '*.mp3*')
        )

        self.audio_file = fd.askopenfilename(
            title = 'Open a file',
            initialdir = '/',
            filetypes = filetypes
        )

        self.model.set_file_path(self.audio_file)


#Start()