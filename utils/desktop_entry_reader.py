from genericpath import isfile
import os
from pathlib import Path
import re
import dotenv
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
        
        entry = DesktopEntry(
            re.search("Name=(.*)", contents).group(1),
            re.search("Exec=(.*)", contents).group(1),
            re.search("Type=(.*)", contents).group(1)
        )
        entry.set_icon_path(re.search("Icon=(.*)", contents).group(1))
        
        if re.search("Terminal=(.*)", contents).group(1) == "True":
            entry.set_terminal()
        
        return entry

    def read_by_name(self, name: str) -> DesktopEntry:
        return self.read(f"{slugify.slugify(name)}.desktop")


if __name__ == "__main__":
    dotenv.load_dotenv()
    
    reader = DesktopEntryReader()
    entry = reader.read_by_name("test-spatie")