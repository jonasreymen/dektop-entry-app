from pathlib import Path

class FileHandler:
    def is_file(self, path: str) -> bool:
        file_path = Path(path).expanduser()
        
        return file_path.is_file()