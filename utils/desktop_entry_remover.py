from pathlib import Path

class DesktopEntryRemover():
    def remove(self, file_path: str) -> None:
        path = Path(file_path).expanduser()
        
        if path.is_file():
            path.unlink()
            return
        
        raise FileNotFoundError("file is not a path")