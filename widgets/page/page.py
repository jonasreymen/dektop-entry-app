from abc import ABC
import tkinter as tk
from widgets.page.page_interface import PageInterface

class Page(tk.Frame, PageInterface, ABC):
    def __init__(self, parent: tk.Frame, name: str) -> None:
        super().__init__(parent, name=name)
        self.name = name
    
    def build(self, data: dict = {}) -> None:
        pass
    
    def load(self, data: dict = {}) -> None:
        self.build(data)
        self.tkraise()