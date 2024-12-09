import tkinter as tk

from builder.standard_page_builder import StandardPageBuilder
from enums.page import Page
from widgets.navigating_button import NavigatingButton

class EditDesktopEntryPageBuilder(StandardPageBuilder):
    def build_title_frame(self, frame: tk.Frame, request_data: dict = {}) -> None:
        tk.Label(frame, text=f"Edit desktop entry '{request_data["file"]}'", background="darkgray").pack(pady=10, padx=10)
    
    def build_content_frame(self, frame: tk.Frame, request_data: dict = {}) -> None:
        pass
    
    def build_toolbar(self, frame: tk.Frame, request_data: dict = {}) -> None:
        NavigatingButton(frame, self.page_navigator, Page.LIST_PAGE.value, text="Home").grid(sticky="nsew", pady=10, padx=10)