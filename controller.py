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
        self.plot_methods = None

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
            duration = round(self.model.display_time_value(), 2)
            highest_resonance = self.model.compute_highest_resonance()
            rt60_diff = self.model.rt60_diff()

            # Update the GUI in View
            self.view.set_file_name(file_path)
            self.view.set_statistics(
                length = duration,
	            freq_great_amp = highest_resonance,
                rt60_diff = rt60_diff
            )
            self.reset_plot_methods()
            self.next_plot()

    def reset_plot_methods(self):
        self.plot_methods = [self.model.waveform, self.model.low, self.model.mid, self.model.high, self.model.plot_rt60, self.model.useful_waveform]

    def next_plot(self):
        self.plot_methods[0]()
        self.plot_methods.append(self.plot_methods.pop(0))
