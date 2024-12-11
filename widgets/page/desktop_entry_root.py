import tkinter as tk

class DesktopEntryRoot(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        
        self.minsize(width=1100, height=500)

        self.title("desktop entry")
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)