from models.desktop_entry_config import Desktop_entry
from jinja2 import Environment, FileSystemLoader
from typeguard import typechecked
import subprocess
from pathlib import Path

@typechecked
class Desktop_entry_writer:
    def __init__(self, folder_path: str = "~/.local/share/applications/") -> None:
        self.path: Path = Path(folder_path).expanduser()

    def write(self, config: Desktop_entry) -> None:
        filepath = self.path / f"{config.name.lower()}.desktop"
        filepath.parent.mkdir(parents=True, exist_ok=True)

        with filepath.open("w") as file:
            file.write(self.generate_template(config))

        filepath.chmod(0o755)
        subprocess.run(["update-desktop-database", self.path.as_posix()])

    def generate_template(self, config: Desktop_entry) -> str:
        env = Environment(loader=FileSystemLoader('.'))
        return env.get_template("templates/template.desktop.j2").render({"config": config})