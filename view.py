import tkinter as tk
from tkinter import ttk
import os

class View(ttk.Frame):
	def __init__(self, parent):
		super().__init__(parent)

		#create widgets
		#load audio button
		self.load_audio_button = ttk.Button(self, text = 'Load Audio', command = self.load_audio_button_clicked)
		self.load_audio_button.grid(row = 0, column = 0, sticky = tk.W)

		#file name label
		self.file_name_label = ttk.Label(self, text = '', font = ('Helvetica', 14, 'italic'))
		self.file_name_label.grid(row = 0, column = 1, sticky = tk.W)

		#statistics label
		self.statistics_label = ttk.Label(self, text = '', font = ('Helvetica', 14, 'bold'))
		self.statistics_label.grid(row = 1, column = 0, sticky = tk.W)

		#audio length label
		self.audio_length_label = ttk.Label(self, text = '')
		self.audio_length_label.grid(row = 2, column = 0, sticky = tk.W)

		#highest resonance label
		self.highest_res_label = ttk.Label(self, text = '')
		self.highest_res_label.grid(row = 3, column = 0, sticky = tk.W)

		#RT60 difference label
		self.rt60_difference_label = ttk.Label(self, text = '')
		self.rt60_difference_label.grid(row = 4, column = 0, sticky = tk.W)

		#next plot button
		self.next_plot_button = ttk.Button(self, text = 'Next Plot', command = self.next_plot_button_clicked)

		#set the controller
		self.controller = None

	def set_controller(self, controller):
		self.controller = controller

	def load_audio_button_clicked(self):
		if self.controller:
			self.controller.select_audio_file()

	def next_plot_button_clicked(self):
		if self.controller:
			self.controller.next_plot()
			pass

	def set_file_name(self, file_path):
		self.file_name_label['text'] = os.path.basename(file_path)

	def set_statistics(self, length, freq_great_amp, rt60_diff):
		self.statistics_label['text'] = 'Audio Statistics:'
		self.audio_length_label['text'] = f'Audio length: {length}s'
		self.highest_res_label['text'] = f'Highest resonance: {freq_great_amp}Hz'
		self.rt60_difference_label['text'] = f'RT60 difference: {rt60_diff}s'
		self.next_plot_button.grid(row = 6, column = 2, padx = 15, sticky = tk.E)
