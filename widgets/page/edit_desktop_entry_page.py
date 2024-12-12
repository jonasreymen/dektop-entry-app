import tkinter as tk

from enums.page_name import PageName
from utils.desktop_entry_reader import DesktopEntryReader
from utils.gui.page_navigator_interface import PageNavigatorInterface
from widgets.desktop_entry_form import DesktopEntryForm
from widgets.navigating_button import NavigatingButton
from widgets.page.standard_page import StandardPage

class EditDesktopEntryPage(StandardPage):
    def __init__(self, parent: tk.Tk, page_navigator: PageNavigatorInterface) -> None:
        super().__init__(parent, PageName.EDIT_PAGE.value)
        self.page_navigator: PageNavigatorInterface = page_navigator
        self.desktop_entry_reader: DesktopEntryReader = DesktopEntryReader()
    
    def build_title_frame(self, frame: tk.Frame, request_data: dict = {}) -> None:
        tk.Label(frame, text=f"Edit desktop entry '{request_data["file"]}'", background="darkgray").pack(pady=10, padx=10)
    
    def build_content_frame(self, frame: tk.Frame, request_data: dict = {}) -> None:
        form = DesktopEntryForm(
            frame,
            self.page_navigator,
            self.desktop_entry_reader.read(request_data["file"])
        )
        
        form.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    
    def build_toolbar(self, frame: tk.Frame, request_data: dict = {}) -> None:
        NavigatingButton(frame, self.page_navigator, PageName.LIST_PAGE.value, text="Home").grid(sticky="nsew", pady=10, padx=10)