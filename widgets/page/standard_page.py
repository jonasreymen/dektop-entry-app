from abc import ABC, abstractmethod
import tkinter as tk

from widgets.page.page import Page

class StandardPage(Page):
    @abstractmethod
    def build_title_frame(self, frame: tk.Frame, request_data: dict = {}) -> None:
        pass
    
    @abstractmethod
    def build_content_frame(self, frame: tk.Frame, request_data: dict = {}) -> None:
        pass
    
    @abstractmethod
    def build_toolbar(self, frame: tk.Frame, request_data: dict = {}) -> None:
        pass
    
    def build(self, request_data: dict = {}) -> None:
        self.__configure_grid()
        self.__build_title_frame(request_data)
        self.__build_content_frame(request_data)
        self.__build_toolbar_frame(request_data)
    
    def __configure_grid(self) -> None:
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1, minsize=750)
        self.grid_columnconfigure(1, weight=0, minsize=300)
        self.grid(row=0, column=0, sticky="nsew")
        
    def __build_title_frame(self, request_data: dict = {}) -> None:
        frame = tk.Frame(self, width=75, background="darkgray", name="title_frame")
        self.build_title_frame(frame, request_data)
        frame.grid(row=0, sticky="nsew", columnspan=2)
    
    def __build_content_frame(self, request_data: dict = {}) -> None:
        frame = tk.Frame(self, width=750, name="content_frame")
        self.build_content_frame(frame, request_data)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
    
    def __build_toolbar_frame(self, request_data: dict = {}) -> None:
        frame = tk.Frame(self, width=300, background="darkgray", name="toolbar_frame")
        self.build_toolbar(frame, request_data)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)