import tkinter as tk

class TkHelper:
    def get_widget_by_name(frame: tk.Frame, name: str) -> tk.Widget:
        """Retrieve a widget by its name within a given frame."""
        for child in frame.winfo_children():
            if child.winfo_name() == name:
                return child
        raise Exception(f"No child wiget found with name: {name}")