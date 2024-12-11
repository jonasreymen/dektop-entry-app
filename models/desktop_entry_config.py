import slugify
from typeguard import typechecked

@typechecked
class DesktopEntry:
    icon_path = ""
    categories = ""
    terminal = False

    def __init__(self, name: str, exec_path: str, entry_type: str = "Application") -> None:
        self.name = name
        self.exec_path = exec_path
        self.entry_type = entry_type

    def set_icon_path(self, icon_path: str) -> None:
        self.icon_path = icon_path

    def set_category(self, category: str) -> None:
        self.categories(category)

    def set_terminal(self) -> None:
        self.terminal = True
    
    def get_file_name(self) -> str:
        name = slugify.slugify(self.name.lower())
        return f"{name}.desktop"