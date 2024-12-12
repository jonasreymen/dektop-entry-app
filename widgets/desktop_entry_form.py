import tkinter as tk
from enums.entry_type import EntryType
from enums.page_name import PageName
from utils.file_handler import FileHandler

from exceptions.validation_exceptions import ValidationError
from models.desktop_entry_config import DesktopEntry
from utils.desktop_entry_writer import Desktop_entry_writer
from utils.gui.page_navigator_interface import PageNavigatorInterface
from widgets.checkbox import Checkbox
from widgets.entry_type_entry import EntryTypeEntry
from widgets.file_explorer_entry import FileExplorerEntry
from tkinter import messagebox

class DesktopEntryForm(tk.Frame):
    def __init__(
        self,
        parent: tk.Widget,
        page_navigator: PageNavigatorInterface,
        desktop_entry: DesktopEntry|None = None
    ) -> None:
        super().__init__(parent)
        
        self.page_navigator: PageNavigatorInterface = page_navigator
        self.file_handler: FileHandler = FileHandler()
        self.desktop_entry = desktop_entry if isinstance(desktop_entry, DesktopEntry) else DesktopEntry()
        
        self.__init_widgets()
    
    def __init_widgets(self) -> None:
        tk.Label(self, text="Name").pack()
        name_entry = tk.Entry(self, name="name")
        if self.desktop_entry.name:
            name_entry.insert(0, self.desktop_entry.name)
        name_entry.pack(padx=10, pady=10)
        
        exec_path_entry = FileExplorerEntry(self, "exec_path", "Execution path")
        if self.desktop_entry.exec_path is not None:
            exec_path_entry.insert(0, self.desktop_entry.exec_path)
        exec_path_entry.pack(padx=10, pady=10)
        
        tk.Label(self, text="Entry_type").pack()
        entry_type_entry = EntryTypeEntry(self, name="entry_type")
        if self.desktop_entry.entry_type:
            entry_type_entry.insert(0, self.desktop_entry.entry_type)
        entry_type_entry.pack(padx=10, pady=10)
        
        icon_path_entry = FileExplorerEntry(self, "icon_path", "Icon path")
        if self.desktop_entry.icon_path is not None:
            icon_path_entry.insert(0, self.desktop_entry.icon_path)
        icon_path_entry.pack(padx=10, pady=10)
        
        Checkbox(self, name="terminal", text="Is terminal", onvalue = 1, offvalue = 0).pack(padx=10, pady=10)
        
        tk.Button(self, text="Add desktop entry", command=lambda: self.save()).pack()
    
    def validate_config(self, config: DesktopEntry) -> list[str]:
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
            
        if errors:
            raise ValidationError(errors)

    def set_data(self) -> DesktopEntry:
        name = self.nametowidget("name").get()
        exec_path = self.nametowidget("exec_path").get()
        entry_type = self.nametowidget("entry_type").get()
        icon = self.nametowidget("icon_path").get()
        
        self.desktop_entry.set_name(name if name else None)
        self.desktop_entry.set_exec_path(exec_path if exec_path else None)
        self.desktop_entry.set_entry_type(entry_type if entry_type else None)
        self.desktop_entry.set_icon_path(icon if icon else None)
        self.desktop_entry.set_terminal(bool(self.nametowidget("terminal").get()))

        return self.desktop_entry

    def save(self) -> None:
        config = self.set_data()
        
        try:
            self.validate_config(config)
        except ValidationError as ve:
            messagebox.showerror("Validation errors", "\n".join(ve.errors))
            return
        
        writer = Desktop_entry_writer()
        writer.write(config)
        
        self.page_navigator.navigate(PageName.LIST_PAGE)