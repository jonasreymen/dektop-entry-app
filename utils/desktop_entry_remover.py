import os
from pathlib import Path

from models.desktop_entry_config import DesktopEntry

class DesktopEntryRemover():
    def __init__(self) -> None:
        self.path = Path(os.getenv("DESKTOP_ENTRY_PATH")).expanduser()
    
    def remove(self, desktop_entry: DesktopEntry) -> None:
        filepath = self.path / desktop_entry.get_file_name()
        
        if filepath.is_file():
            filepath.unlink()
            return
        
        raise FileNotFoundError("file is not a path")