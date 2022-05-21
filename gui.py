class Gui:
    def __init__(self):
        self.windows = list()
        self.window_names = ["greeting", "query1"]
    def add_window(self, window):
        self.windows.add(window)

class Window(Gui):
    def __init__(self, name):
        self.name = name
        self.widgets = list()
    def start(self):
        window = tk.Tk()
    def create(self):
        
    def pack(self):
        for widget in self.widgets:
            widget.pack()
    def greeting(self):
        window = tk.Tk()
        greeting = tk.Label(text = "Welcome to Venue Planner!")
        instructions = tk.Label(pady = 100,
        text = "This application automatically assigns people to seats based on the information you provide.\n Click the continue button to get started.")
        button = tk.Button(text = "Continue", command = "open_new_window")



        greeting.pack()
        instructions.pack()
        button.pack()
        window.mainloop()
    def exit_window(self, current_window):
        window = top_level(current_window)

class Widget(Window):
    def __init__(self, name, type):
        self.name = name
        self.type = type
