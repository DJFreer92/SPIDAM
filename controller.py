from tkinter import filedialog as fd

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.audio_file = ''
        self.plot_methods = None

    def select_audio_file(self):
        # Specify the files types to allow the user to select
        filetypes = (
            ('audio files', ('*.wav','*.mp3')),
            ('mp3 files', '*.mp3*'),
            ('wav files', '*.wav')
        )

        # Open a popup for the user to select a file of the specified types
        self.audio_file = fd.askopenfilename(
            title = 'Open a file',
            initialdir = '/',
            filetypes = filetypes
        )

        # If the user selected an audio file
        if self.audio_file:
            # Set the file path in the model
            self.model.set_file_path(self.audio_file)

            # Analyze the data and display it
            self.analyze_and_display()

    def analyze_and_display(self):
        # If there is no selected audio file, exit the method
        if not self.audio_file: return

        # Set the file path in the model
        self.model.set_file_path(self.audio_file)

        # Perform analysis using the model
        duration = round(self.model.display_time_value(), 2)
        highest_resonance = self.model.compute_highest_resonance()
        rt60_diff = self.model.rt60_diff()

        # Update the file name and statistic in the view
        self.view.set_file_name(self.audio_file)
        self.view.set_statistics(
            length = duration,
            freq_great_amp = highest_resonance,
            rt60_diff = rt60_diff
        )

        # Put the plot methods in order
        self.reset_plot_methods()

        # Display the first plot
        self.next_plot()

    def reset_plot_methods(self):
        # Get all the methods that generate a plot from the model
        self.plot_methods = [self.model.waveform, self.model.low, self.model.mid, self.model.high, self.model.plot_rt60, self.model.useful_waveform]

    def next_plot(self):
        # Display the next plot
        self.plot_methods[0]()

        # Move the displayed model to the end of the cycle
        self.plot_methods.append(self.plot_methods.pop(0))
