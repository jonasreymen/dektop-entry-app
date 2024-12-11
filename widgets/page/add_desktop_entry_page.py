import tkinter as tk

from enums.page_name import PageName
from utils.gui.page_navigator_interface import PageNavigatorInterface
from widgets.desktop_entry_form import AddDesktopEntryForm
from widgets.navigating_button import NavigatingButton
from widgets.page.standard_page import StandardPage

class AddDesktopEntryPage(StandardPage):
    def __init__(self, parent: tk.Tk, page_navigator: PageNavigatorInterface) -> None:
        super().__init__(parent, PageName.ADD_PAGE.value)
        self.page_navigator = page_navigator
    
    def build_title_frame(self, frame: tk.Frame, request_data: dict = {}) -> None:
        tk.Label(frame, text="Add Desktop Entry", background="darkgray").pack(pady=10, padx=10)
    
    def build_content_frame(self, frame: tk.Frame, request_data: dict = {}) -> None:
        form = AddDesktopEntryForm(frame, self.page_navigator)
        
        form.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    
    def build_toolbar(self, frame: tk.Frame, request_data: dict = {}) -> None:
        NavigatingButton(frame, self.page_navigator, PageName.LIST_PAGE.value, text="Home").grid(sticky="nsew", pady=10, padx=10)