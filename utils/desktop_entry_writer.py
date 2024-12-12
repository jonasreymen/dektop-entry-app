import os
from models.desktop_entry_config import DesktopEntry
from jinja2 import Environment, FileSystemLoader
from typeguard import typechecked
import subprocess
from pathlib import Path

@typechecked
class Desktop_entry_writer:
    def __init__(self) -> None:
        self.path: Path = Path(os.getenv("DESKTOP_ENTRY_PATH")).expanduser()

    def write(self, config: DesktopEntry) -> None:
        if config.filename and config.filename != config.get_file_name():
            old_filepath = self.path / config.filename
            old_filepath.unlink()
        
        filepath = self.path / config.get_file_name()
        filepath.parent.mkdir(parents=True, exist_ok=True)

        with filepath.open("w") as file:
            file.write(self.generate_template(config))
        
        config.set_filename(config.get_file_name())

        filepath.chmod(0o755)
        subprocess.run(["update-desktop-database", self.path.as_posix()])

    def generate_template(self, config: DesktopEntry) -> str:
        env = Environment(loader=FileSystemLoader('.'))
        return env.get_template("templates/template.desktop.j2").render({
            "name": config.name,
            "exec_path": config.exec_path,
            "icon_path": (config.icon_path if config.icon_path else ""),
            "entry_type": config.entry_type,
            "terminal": config.terminal
        })