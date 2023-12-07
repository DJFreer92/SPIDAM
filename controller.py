from view import View
from model import Model
from tkinter import filedialog as fd
import tkinter as tk

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

        if self.audio_file:
            self.model.set_file_path(self.audio_file)
            self.view.set_file_name(self.audio_file)  # Update file name in the view
            self.view.set_statistics(length=0, freq_great_amp=0, rt60_diff=0)  # Clear previous statistics
            self.view.set_plot(None)  # Clear previous plot

    def analyze_and_display(self):
        file_path = self.file_path_entry.get()

        if file_path:
            self.model.set_file_path(file_path)

            # Perform analysis using the Model
            highest_resonance = self.model.compute_highest_resonance()
            duration = self.model.display_time_value()

            # Update the GUI in View
            self.view.set_file_name(file_path)
            self.view.set_statistics(length=duration, freq_great_amp=highest_resonance,rt60_diff=0)  # Replace 0 with actual RT60 difference
            self.view.set_plot(self.model.waveform())  # Display waveform



def main():
    root = tk.Tk()
    model_instance = Model()
    view_instance = View(root)
    controller_instance = Controller(root, model_instance, view_instance)
    root.mainloop()

if __name__ == "__main__":
    main()