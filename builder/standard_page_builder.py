from abc import abstractmethod
import tkinter as tk
from builder.page_builder import PageBuilder
from utils.gui.page_navigator_interface import PageNavigatorInterface

class StandardPageBuilder(PageBuilder):
    @abstractmethod
    def build_title_frame(self, frame: tk.Frame, page_navigator: PageNavigatorInterface) -> None:
        pass
    
    @abstractmethod
    def build_content_frame(self, frame: tk.Frame, page_navigator: PageNavigatorInterface) -> None:
        pass
    
    @abstractmethod
    def build_toolbar(self, frame: tk.Frame, page_navigator: PageNavigatorInterface) -> None:
        pass
    
    def build(self, parent: tk.Frame, page_navigator: PageNavigatorInterface) -> None:
        self.__configure_grid(parent)
        self.__build_title_frame(parent, page_navigator)
        self.__build_content_frame(parent, page_navigator)
        self.__build_toolbar_frame(parent, page_navigator)
    
    def __configure_grid(self, parent: tk.Frame) -> None:
        parent.grid_rowconfigure(0, weight=0)
        parent.grid_rowconfigure(1, weight=1)
        parent.grid_columnconfigure(0, weight=1, minsize=750)
        parent.grid_columnconfigure(1, weight=0, minsize=300)
        parent.grid(row=0, column=0, sticky="nsew")
        
    def __build_title_frame(self, parent: tk.Frame, page_navigator: PageNavigatorInterface) -> None:
        frame = tk.Frame(parent, width=75, background="darkgray", name="title_frame")
        self.build_title_frame(frame, page_navigator)
        frame.grid(row=0, sticky="nsew", columnspan=2)
    
    def __build_content_frame(self, parent: tk.Frame, page_navigator: PageNavigatorInterface) -> None:
        frame = tk.Frame(parent, width=750, name="content_frame")
        self.build_content_frame(frame, page_navigator)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
    
    def __build_toolbar_frame(self, parent: tk.Frame, page_navigator: PageNavigatorInterface) -> None:
        frame = tk.Frame(parent, width=300, background="darkgray", name="toolbar_frame")
        self.build_toolbar(frame, page_navigator)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)