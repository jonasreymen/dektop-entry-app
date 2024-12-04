import tkinter as tk
from builder.standard_page_builder import StandardPageBuilder
from enums.page import Page
from utils.gui.page_navigator_interface import PageNavigatorInterface
from widgets.navigating_button import NavigatingButton

from pathlib import Path
from tkinter.ttk import Treeview

class ListDesktopEntriesPageBuilder(StandardPageBuilder):
    def build_title_frame(self, frame: tk.Frame, page_navigator: PageNavigatorInterface) -> None:
        label = tk.Label(frame, text="List of Desktop Entries", background="darkgray")
        label.pack(pady=10, padx=10)
    
    def build_content_frame(self, frame: tk.Frame, page_navigator: PageNavigatorInterface) -> None:
        path = Path("~/.local/share/applications/").expanduser()
        
        gen = path.glob("*.desktop")
        
        self.tree = Treeview(frame, name="desktop_entry_tree")
        self.tree.heading("#0", text="File")
        for file in gen:
            self.tree.insert("", tk.END, text=file.name, iid=file.as_posix())
        self.tree.pack(padx=10, pady=10)
    
    def build_toolbar(self, frame: tk.Frame, page_navigator: PageNavigatorInterface) -> None:
        NavigatingButton(frame, page_navigator, Page.ADD_PAGE.value, text="Add a new desktop entry").grid(sticky="nsew", pady=10, padx=10)
        
        frame.master.nametowidget("content_frame.desktop_entry_tree")
        