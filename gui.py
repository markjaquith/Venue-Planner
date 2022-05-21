
from logging import root
import tkinter as tk
import venue

class Gui:
    def __init__(self):
        self.introduce()
    def newWindow(self):
        self.window = tk.Tk()
        self.window.title("Venue Planner")
        self.window.geometry("1920x1080")

    # Displays opening message
    def introduce(self):
        self.newWindow()
        # self.window = tk.Tk()
        # self.window.title("Venue Planner")
        # self.window.geometry("1920x1080")
        frame = tk.Frame()
        tk.Label(frame, 
            padx = 50,
            text = "Welcome to Venue Planner!"
        ).pack()
        tk.Label(
            pady = 50,
            text = "This application automatically assigns seats based on information provided."
        ).pack()
        tk.Label(
            text = "press the button to begin:"
        ).pack()
        tk.Button(
            text = "begin",
            command = self.query1
            ).pack()
        tk.mainloop()
    # querys for name of venue
    def query1(self):
        self.window.withdraw()
        self.newWindow()

if __name__ == "__main__":
    gui = Gui()
    global venue
    venue = venue()
