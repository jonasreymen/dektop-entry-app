import tkinter as tk

from builder.standard_page_builder import StandardPageBuilder
from enums.page import Page
from utils.gui.page_navigator_interface import PageNavigatorInterface
from widgets.add_desktop_entry_form import AddDesktopEntryForm
from widgets.navigating_button import NavigatingButton

class AddDesktopEntryPageBuilder(StandardPageBuilder):
    def build_title_frame(self, frame: tk.Frame, page_navigator: PageNavigatorInterface) -> None:
        label = tk.Label(frame, text="Add Desktop Entry", background="darkgray")
        label.pack(pady=10, padx=10)
    
    def build_content_frame(self, frame: tk.Frame, page_navigator: PageNavigatorInterface) -> None:
        form = AddDesktopEntryForm(frame, page_navigator)
        
        form.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    
    def build_toolbar(self, frame: tk.Frame, page_navigator: PageNavigatorInterface) -> None:
        NavigatingButton(frame, page_navigator, Page.LIST_PAGE.value, text="Home").grid(sticky="nsew", pady=10, padx=10)