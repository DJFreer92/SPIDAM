import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

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

		#frequency of greatest amplitude label
		self.frequency_greatest_amplitude_label = ttk.Label(self, text = '')
		self.frequency_greatest_amplitude_label.grid(row = 3, column = 0, sticky = tk.W)

		#RT60 difference label
		self.rt60_difference_label = ttk.Label(self, text = '')
		self.rt60_difference_label.grid(row = 4, column = 0, sticky = tk.W)

		#canvas for plots
		self.canvas = None

		#next plot button
		self.next_plot_button = ttk.Button(self, text = 'Next Plot', command = self.next_plot_button_clicked)
		self.next_plot_button.grid(row = 6, column = 2, padx = 15, sticky = tk.E)

		#tests
		self.set_file_name("test_name.wav")
		self.set_statistics(length = 20, freq_great_amp = 12, rt60_diff = 5)

		#set the controller
		self.controller = None

	def set_controller(self, controller):
		self.controller = controller

	def load_audio_button_clicked(self):
		if self.controller:
			self.controller.select_audio_file()

	def next_plot_button_clicked(self):
		if self.controller:
			#self.controller.next_plot()
			pass

	def set_file_name(self, file_name):
		self.file_name_label['text'] = file_name

	def set_statistics(self, length, freq_great_amp, rt60_diff):
		self.statistics_label['text'] = 'Audio Statistics:'
		self.audio_length_label['text'] = f'Audio length: {length}s'
		self.frequency_greatest_amplitude_label['text'] = f'Frequency of greatest amplitude: {freq_great_amp}Hz'
		self.rt60_difference_label['text'] = f'RT60 difference: {rt60_diff}s'

	def set_plot(self, plot):
		#if a canvas has been created previously delete it
		if self.canvas:
			self.canvas.delete('all')

		#creating the Tkinter canvas
		#containing the Matplotlib figure
		self.canvas = FigureCanvasTkAgg(plot, self)
		self.canvas.draw()

		#placing the canvas on the Tkinter window
		self.canvas.get_tk_widget().pack()

		#creating the Matplotlib toolbar
		toolbar = NavigationToolbar2Tk(self.canvas, self)
		toolbar.update()

		#placing the toolbar on the Tkinter window
		self.canvas.get_tk_widget().pack()

		#position the canvas on the Tkinter window
		self.canvas.get_tk_widget().grid(row = 5, column = 0, sticky = tk.W)
