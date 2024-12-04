import tkinter as tk

class Checkbox(tk.Checkbutton):
    def __init__(self, parent: tk.Frame, name: str, *args, **kwargs) -> None:
        self.value = tk.IntVar()
        
        super().__init__(parent, name=name, variable=self.value, *args, **kwargs)
        
    def get(self) -> tk.IntVar:
        return self.value.get()