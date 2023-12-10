from model import Model
from view import View
from controller import Controller
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # App title
        self.title('Scientific Python Interactive Data Acoustic Modeling')

        # Disallow the user to resize the app window
        self.resizable(width = False, height = False)

        # Create a model
        model = Model()

        # Create a view and place it on the root window
        view = View(self)
        view.grid(row = 0, column = 0, padx = 10, pady = 10)

        # Create a controller
        controller = Controller(model, view)

        # Set the controller in the view
        view.set_controller(controller)


if __name__ == '__main__':
    # Initialize the app
    app = App()
    app.mainloop()
