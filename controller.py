from view import View
from model import Model
from tkinter import filedialog as fd
import tkinter as tk

class Controller:
    plt_num = 0
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
            self.analyze_and_display()

    def analyze_and_display(self):
        file_path = self.audio_file

        if file_path:
            self.model.set_file_path(file_path)

            # Perform analysis using the Model
            highest_resonance = self.model.compute_highest_resonance()
            duration = self.model.display_time_value()

            # Update the GUI in View
            self.view.set_file_name(file_path)
            self.view.set_statistics(length=duration, freq_great_amp=highest_resonance, rt60_diff=0)  # Replace 0 with actual RT60 difference

    def next_plot(self):
        Controller.plt_num += 1
        if Controller.plt_num == 1:
            self.model.waveform()
        elif Controller.plt_num == 2:
            self.model.low()
        elif Controller.plt_num == 3:
            self.model.mid()
        elif Controller.plt_num == 4:
            self.model.high()
        elif Controller.plt_num == 5:
            self.model.plot_rt60()
        # elif Controller.plt_num == 6:
        #     Model.suprise()
        else:
            return
