from view import View
#from model import Model
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


#Controller is to be written last
class Controller:
    def __init__(self, model, view):
        #self.model = Model
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


#Start()