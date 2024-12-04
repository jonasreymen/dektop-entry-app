import tkinter as tk
from builder.page_builder import PageBuilder

class Page(tk.Frame):
    def __init__(self, parent: "PageContainer", name: str, page_builder: PageBuilder) -> None:
        super().__init__(parent, name=name)
        
        self.name = name
        page_builder.build(self, parent.navigator)