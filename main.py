import tkinter as tk
import venue, gui




if __name__ == "__main__":
    gui = Gui()
    for window in gui.window_names:
        gui.add_window(window)
    for window in gui.windows:
        
    for window in gui.windows:
        window.start()
        window.create()


