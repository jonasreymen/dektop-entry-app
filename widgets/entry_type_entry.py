from tkinter import ttk

from enums.entry_type import EntryType

class EntryTypeEntry(ttk.Combobox):
    def __init__(self, parent, *args, **kwargs) -> None:
        super().__init__(parent, values=EntryType.all(), *args, **kwargs)