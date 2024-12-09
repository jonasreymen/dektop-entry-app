import tkinter as tk
from builder.standard_page_builder import StandardPageBuilder
from enums.page import Page
from utils.desktop_entry_remover import DesktopEntryRemover
from utils.gui.page_navigator_interface import PageNavigatorInterface
from widgets.navigating_button import NavigatingButton

from pathlib import Path
from tkinter.ttk import Treeview
from tkinter import messagebox

class ListDesktopEntriesPageBuilder(StandardPageBuilder):
    def __init__(self, page_navigator: PageNavigatorInterface) -> None:
        super().__init__(page_navigator)
        
        self.tree = None
        self.edit_button: NavigatingButton = None
        self.delete_button: tk.Button = None
        self.desktop_entry_remover: DesktopEntryRemover = DesktopEntryRemover()
    
    def build_title_frame(self, frame: tk.Frame, request_data: dict = {}) -> None:
        tk.Label(frame, text="List of Desktop Entries", background="darkgray").pack(pady=10, padx=10)
    
    def build_content_frame(self, frame: tk.Frame, request_data: dict = {}) -> None:
        path = Path("~/.local/share/applications/").expanduser()
        
        gen = path.glob("*.desktop")
        
        self.tree = Treeview(frame, name="desktop_entry_tree")
        self.tree.heading("#0", text="File")
        for file in gen:
            self.tree.insert("", tk.END, text=file.name, iid=file.as_posix())
        self.tree.pack(padx=10, pady=10, fill='both')
        self.tree.bind("<<TreeviewSelect>>", self.selection_callback)
    
    def build_toolbar(self, frame: tk.Frame, request_data: dict = {}) -> None:
        NavigatingButton(frame, self.page_navigator, Page.ADD_PAGE.value, text="Add a new desktop entry").grid(sticky="nsew", pady=10, padx=10)
        self.edit_button = NavigatingButton(
            frame,
            self.page_navigator,
            Page.EDIT_PAGE.value,
            lambda: {"file": self.get_selected_item()},
            text="Edit desktop entry"
        )
        self.delete_button = tk.Button(frame, text="Delete", command=self.delete_desktop_entry)
        
        self.edit_button["state"] = "disabled"
        self.delete_button["state"] = "disabled"
        
        self.edit_button.grid(sticky="nsew", pady=10, padx=10)
        self.delete_button.grid(sticky="nsew", pady=10, padx=10)
    
    def selection_callback(self, event) -> None:
        if self.get_selected_item() is not None:
            self.edit_button["state"] = "normal"
            self.delete_button["state"] = "normal"
            return
        
        self.edit_button["state"] = "disabled"
        self.delete_button["state"] = "disabled"
    
    def get_selected_item(self) -> str | None:
        selected_item = self.tree.selection()
        
        if selected_item:
            return selected_item[0]
        return None

    def delete_desktop_entry(self) -> None:
        selected_item = self.get_selected_item()
        if selected_item:
            try:
                self.desktop_entry_remover.remove(selected_item)
                self.tree.delete(selected_item)
            except FileNotFoundError:
                messagebox.showerror("Deletion error", "File not found")