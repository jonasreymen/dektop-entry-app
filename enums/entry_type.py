from enum import StrEnum

class EntryType(StrEnum):
    APPLICATION: str = "Application"
    LINK: str = "Link"
    DIRECTORY: str = "Directory"
    
    def all() -> tuple:
        return (EntryType.APPLICATION.value, EntryType.LINK.value, EntryType.DIRECTORY.value)