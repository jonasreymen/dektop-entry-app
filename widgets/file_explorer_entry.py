from tkinter import Entry, filedialog
import tkinter as tk

class FileExplorerEntry(tk.Frame, Entry):
    def __init__(self, parent: tk.Frame, field_name: str, label: str) -> None:
        super().__init__(parent, highlightbackground="darkgray", highlightthickness=1, name=field_name, padx=10, pady=10)
        self.field_name = field_name
        self.label = label
        
        self.__init_widgets()
        
        self.entry: Entry = self.nametowidget(self.field_name)
    
    def __init_widgets(self) -> None:
        tk.Label(self, text=self.label).grid(row=0, columnspan=3)
        tk.Entry(self, name=self.field_name).grid(row=1, columnspan=2, padx=10)
        tk.Button(self,text="open file explorer", command=lambda: self.handle_file_dialog()).grid(row=1, column=2)
    
    def handle_file_dialog(self) -> None:
        file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("All files", "*.*")])
        
        if not file_path:
            return
        
        self.entry.delete(0, tk.END)
        self.entry.insert(0, file_path)
    
    def insert(self, index: str | int, string: str) -> None:
        self.entry.insert(index, string)
    
    def get(self) -> str:
        return self.entry.get()
