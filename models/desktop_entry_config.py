import slugify
from typeguard import typechecked
from enums.entry_type import EntryType

@typechecked
class DesktopEntry:
    name: str|None = None
    exec_path: str|None = None
    entry_type: str|None = EntryType.APPLICATION.value
    icon_path: str|None = None
    categories: str|None = None
    terminal: bool = False
    filename: str|None = None
    
    def set_name(self, name: str|None) -> None:
        self.name = name
    
    def set_exec_path(self, exec_path: str|None) -> None:
        self.exec_path = exec_path
    
    def set_entry_type(self, entry_type: str|None) -> None:
        self.entry_type = entry_type

    def set_icon_path(self, icon_path: str|None) -> None:
        self.icon_path = icon_path

    def set_category(self, category: str|None) -> None:
        self.categories = category

    def set_terminal(self, is_terminal: bool) -> None:
        self.terminal = is_terminal
    
    def set_filename(self, filename: str|None) -> None:
        self.filename = filename
    
    def get_file_name(self) -> str:
        name = slugify.slugify(self.name.lower())
        return f"{name}.desktop"