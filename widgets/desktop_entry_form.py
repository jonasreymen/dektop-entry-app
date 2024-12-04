import tkinter as tk
from enums.entry_type import EntryType
from enums.page import Page
from utils.file_handler import FileHandler

from exceptions.validation_exceptions import ValidationError
from models.desktop_entry_config import Desktop_entry
from utils.desktop_entry_writer import Desktop_entry_writer
from utils.gui.page_navigator_interface import PageNavigatorInterface
from widgets.checkbox import Checkbox
from widgets.entry_type_entry import EntryTypeEntry
from widgets.file_explorer_entry import FileExplorerEntry
from tkinter import messagebox

class AddDesktopEntryForm(tk.Frame):
    def __init__(self, parent: tk.Widget, page_navigator: PageNavigatorInterface) -> None:
        super().__init__(parent)
        
        self.page_navigator: PageNavigatorInterface = page_navigator
        self.file_handler: FileHandler = FileHandler()
        
        self.__init_widgets()
    
    def __init_widgets(self) -> None:
        tk.Label(self, text="Name").pack()
        tk.Entry(self, name="name", validate="focusout").pack(padx=10, pady=10)
        
        FileExplorerEntry(self, "exec_path", "Execution path").pack(padx=10, pady=10)
        
        tk.Label(self, text="Entry_type").pack()
        entry_type_entry = EntryTypeEntry(self, name="entry_type")
        entry_type_entry.insert(0, EntryType.APPLICATION.value)
        entry_type_entry.pack(padx=10, pady=10)
        
        FileExplorerEntry(self, "icon_path", "Icon path").pack(padx=10, pady=10)
        
        Checkbox(self, name="terminal", text="Is terminal", onvalue = 1, offvalue = 0).pack(padx=10, pady=10)
        
        tk.Button(self, text="Add desktop entry", command=lambda: self.save()).pack()
    
    def validate_config(self, config: Desktop_entry) -> list[str]:
        errors = []
        
        if not config.name:
            errors.append("Name is required")
        
        if not config.exec_path:
            errors.append("Execution path is required")
        
        if config.exec_path and not self.file_handler.is_file(config.exec_path):
            errors.append("Execution path is not a valid path")
        
        if not config.entry_type:
            errors.append("Entry type is required")
        
        if config.entry_type and config.entry_type not in EntryType.all():
            errors.append(f"Incorrect entry type, please use one of {EntryType.all()}")
        
        if config.icon_path and not self.file_handler.is_file(config.icon_path):
            errors.append("Icon path is not a valid path")

        return errors

    def get_data(self) -> Desktop_entry:
        name = self.nametowidget("name").get()
        exec_path = self.nametowidget("exec_path").get()
        entry_type = self.nametowidget("entry_type").get()
        icon = self.nametowidget("icon_path").get()

        config = Desktop_entry(name,exec_path,entry_type)
        if icon:
            config.icon_path = icon
        
        terminal = self.nametowidget("terminal").get()
        config.terminal = bool(terminal)
        
        errors = self.validate_config(config)
        if len(errors):
            raise ValidationError(errors)

        return config

    def save(self) -> None:
        try:
            config = self.get_data()
        except ValidationError as ve:
            messagebox.showerror("Validation errors", "\n".join(ve.errors))
            return
        
        writer = Desktop_entry_writer()
        writer.write(config)
        
        self.page_navigator.navigate(Page.LIST_PAGE)