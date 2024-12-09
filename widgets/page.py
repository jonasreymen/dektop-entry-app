import tkinter as tk

from builder.page_builder import PageBuilder

class Page(tk.Frame):
    def __init__(self, parent: "PageContainer", name: str, builder: PageBuilder) -> None:
        super().__init__(parent, name=name)
        
        self.name = name
        self.page_builder = builder
    
    def build(self, data: dict = {}) -> None:
        self.page_builder.build(self, data)
    
    def load(self, data: dict = {}) -> None:
        self.build(data)
        self.tkraise()