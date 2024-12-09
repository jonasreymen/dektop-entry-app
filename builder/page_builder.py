from abc import ABC, abstractmethod
import tkinter as tk

from utils.gui.page_navigator_interface import PageNavigatorInterface

class PageBuilder(ABC):
    def __init__(self, page_navigator: PageNavigatorInterface) -> None:
        self.page_navigator = page_navigator
    
    @abstractmethod
    def build(self, parent: tk.Frame, request_data: dict = {}) -> None:
        pass