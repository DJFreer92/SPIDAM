import tkinter as tk
from tkinter import ttk
import os

class View(ttk.Frame):
	def __init__(self, parent):
		super().__init__(parent)

		# Create widgets
		# Load audio button
		self.load_audio_button = ttk.Button(self, text = 'Load Audio', command = self.load_audio_button_clicked)
		self.load_audio_button.grid(row = 0, column = 0, sticky = tk.W)

		# File name label
		self.file_name_label = ttk.Label(self, text = '', font = ('Helvetica', 14, 'italic'))
		self.file_name_label.grid(row = 0, column = 1, sticky = tk.W)

		# Statistics label
		self.statistics_label = ttk.Label(self, text = '', font = ('Helvetica', 14, 'bold'))
		self.statistics_label.grid(row = 1, column = 0, sticky = tk.W)

		# Audio length label
		self.audio_length_label = ttk.Label(self, text = '')
		self.audio_length_label.grid(row = 2, column = 0, sticky = tk.W)

		# Highest resonance label
		self.highest_res_label = ttk.Label(self, text = '')
		self.highest_res_label.grid(row = 3, column = 0, sticky = tk.W)

		# RT60 difference label
		self.rt60_difference_label = ttk.Label(self, text = '')
		self.rt60_difference_label.grid(row = 4, column = 0, sticky = tk.W)

		# Next plot button
		self.next_plot_button = ttk.Button(self, text = 'Next Plot', command = self.next_plot_button_clicked)

		# Set the controller
		self.controller = None

	def set_controller(self, controller):
		# Set the controller
		self.controller = controller

	def load_audio_button_clicked(self):
		# Tell the controller to let the user select an audio file
		if self.controller:
			self.controller.select_audio_file()

	def next_plot_button_clicked(self):
		# Tell the controller to switch to the next plot
		if self.controller:
			self.controller.next_plot()

	def set_file_name(self, file_path):
		# Extract the file name from the file path and assign it to the file name label
		self.file_name_label['text'] = os.path.basename(file_path)

	def set_statistics(self, length, freq_great_amp, rt60_diff):
		# Assign statistics to their respective labels
		self.statistics_label['text'] = 'Audio Statistics:'
		self.audio_length_label['text'] = f'Audio length: {length}s'
		self.highest_res_label['text'] = f'Highest resonance: {freq_great_amp}Hz'
		self.rt60_difference_label['text'] = f'RT60 difference: {rt60_diff}s'

		# Put to next plot button on the tkinter window
		self.next_plot_button.grid(row = 6, column = 2, padx = 15, sticky = tk.E)
