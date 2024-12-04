from abc import ABC, abstractmethod
import tkinter as tk

from utils.gui.page_navigator_interface import PageNavigatorInterface

class PageBuilder(ABC):
    @abstractmethod
    def build(self, parent: tk.Frame, page_navigator: PageNavigatorInterface) -> None:
        pass