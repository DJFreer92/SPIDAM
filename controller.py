from audio_app import App
from view import View
#from model import Model
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
gfile = ''
# create the root window
root = tk.Tk()
root.title('Tkinter Open File Dialog')
root.resizable(False, False)
root.geometry('300x150')

def select_file():
    filetypes = (
        ('wav files', '*.wav'),
        ('mp3 files', '*.mp3*')
        )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    gfile = filename
# tkinter.messagebox — Tkinter message prompts
    showinfo(
        title='Selected File',
        message=filename
        )

gfile_label = ttk.Label(root, text=gfile)
gfile_label.pack(side="bottom")

# open button
open_button = ttk.Button(
    root,
    text='Open a File',
    command=select_file
    )
open_button.pack(expand=True)
# run the application
root.mainloop()





#Controller is to be written last
#class Controller:
    #def __init__(self, Model, View):
        #self.model = Model
        #self.view = View
    #def Start():


#Start()