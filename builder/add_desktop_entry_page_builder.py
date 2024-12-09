import tkinter as tk

from builder.standard_page_builder import StandardPageBuilder
from enums.page import Page
from widgets.desktop_entry_form import AddDesktopEntryForm
from widgets.navigating_button import NavigatingButton

class AddDesktopEntryPageBuilder(StandardPageBuilder):
    def build_title_frame(self, frame: tk.Frame, request_data: dict = {}) -> None:
        tk.Label(frame, text="Add Desktop Entry", background="darkgray").pack(pady=10, padx=10)
    
    def build_content_frame(self, frame: tk.Frame, request_data: dict = {}) -> None:
        form = AddDesktopEntryForm(frame, self.page_navigator)
        
        form.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    
    def build_toolbar(self, frame: tk.Frame, request_data: dict = {}) -> None:
        NavigatingButton(frame, self.page_navigator, Page.LIST_PAGE.value, text="Home").grid(sticky="nsew", pady=10, padx=10)