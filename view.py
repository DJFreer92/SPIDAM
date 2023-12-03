import tkinter as tk
from tkinter import ttk

class View(ttk.Frame):
	def __init__(self, parent):
		super().__init__(parent)

		#create widgets
		#load audio button
		self.load_audio_button = ttk.Button(self, text = 'Load Audio', command = self.load_audio_button_clicked)
		self.load_audio_button.grid(row = 0, column = 0, sticky = tk.W)

		#file name label
		self.file_name_label = ttk.Label(self, text = '')
		self.file_name_label.grid(row = 0, column = 1, sticky = tk.W)

		#statistics label
		self.statistics_label = ttk.Label(self, text = 'Audio Statistics:')
		self.statistics_label.grid(row = 1, column = 0)

		#audio length label
		self.audio_length_label = ttk.Label(self, text = 'Audio length: ')
		self.audio_length_label.grid(row = 2, column = 0, sticky = tk.W)

		#frequency of greatest amplitude label
		self.frequency_greatest_amplitude_label = ttk.Label(self, text = 'Frequency of greatest amplitude: ')
		self.frequency_greatest_amplitude_label.grid(row = 3, column = 0, sticky = tk.W)

		#RT60 difference label
		self.rt60_difference_label = ttk.Label(self, text = 'RT60 difference: ')
		self.rt60_difference_label.grid(row = 4, column = 0, sticky = tk.W)

		#TO DO: Plots here

		#next plot button
		self.next_plot_button = ttk.Button(self, text = 'Next Plot', command = self.next_plot_button_clicked)
		self.next_plot_button.grid(row = 6, column = 2, padx = 15)

		#tests
		self.set_file_name("test_name.wav")
		self.set_audio_length(20)
		self.set_frequency_greatest_amplitude(12)
		self.set_rt60_difference(5)

		#set the controller
		self.controller = None

	def set_controller(self, controller):
		self.controller = controller

	def load_audio_button_clicked(self):
		if self.controller:
			#self.controller.load_audio_file()
			pass

	def next_plot_button_clicked(self):
		if self.controller:
			#self.controller.next_plot()
			pass

	def set_file_name(self, file_name):
		self.file_name_label['text'] = file_name

	def set_audio_length(self, audio_length):
		self.audio_length_label['text'] += f'{audio_length}s'

	def set_frequency_greatest_amplitude(self, frequency_greatest_amplitude):
		self.frequency_greatest_amplitude_label['text'] += f'{frequency_greatest_amplitude}Hz'

	def set_rt60_difference(self, rt60_difference):
		self.rt60_difference_label['text'] += f'{rt60_difference}s'

	def set_plot(self, plot):
		#TO DO: set the plot
		pass