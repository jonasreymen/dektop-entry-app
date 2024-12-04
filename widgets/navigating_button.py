import tkinter as tk

from utils.gui.page_navigator_interface import PageNavigatorInterface

class NavigatingButton(tk.Button):
    def __init__(self, parent: tk.Frame, page_navigator: PageNavigatorInterface, page_name: str, **kw) -> None:
        super().__init__(parent, kw, command=lambda: self.page_navigator.navigate(self.page_name))
        self.page_navigator = page_navigator
        self.page_name = page_name