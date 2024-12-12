from genericpath import isfile
import os
from pathlib import Path
import re
import slugify
from models.desktop_entry_config import DesktopEntry

class DesktopEntryReader:
    def __init__(self) -> None:
        self.path = Path(os.getenv("DESKTOP_ENTRY_PATH")).expanduser()
    
    def read(self, file_name: str) -> DesktopEntry:
        path = self.path / file_name
        
        if not path.is_file():
            raise FileNotFoundError(f"Could not find file for path '{path.absolute()}'")
        
        contents = path.read_text()
        
        entry = DesktopEntry()
        
        entry.set_name(re.search("Name=(.*)", contents).group(1))
        entry.set_exec_path(re.search("Exec=(.*)", contents).group(1))
        entry.set_entry_type(re.search("Type=(.*)", contents).group(1))
        entry.set_icon_path(re.search("Icon=(.*)", contents).group(1))
        entry.set_terminal(re.search("Terminal=(.*)", contents).group(1) == "True")
        entry.set_filename(file_name)
        
        return entry

    def read_by_name(self, name: str) -> DesktopEntry:
        return self.read(f"{slugify.slugify(name)}.desktop")