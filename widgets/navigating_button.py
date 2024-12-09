import tkinter as tk

from utils.gui.page_navigator_interface import PageNavigatorInterface

class NavigatingButton(tk.Button):
    def __init__(
        self,
        parent: tk.Frame,
        page_navigator: PageNavigatorInterface,
        page_name: str,
        request_data_callback = None,
        **kw
    ) -> None:
        super().__init__(
            parent,
            command=self.command_callback,
            **kw
        )
        self.page_navigator = page_navigator
        self.page_name = page_name
        self.request_data_callback = request_data_callback if request_data_callback is not None else lambda: {}
    
    def command_callback(self) -> None:
        self.page_navigator.navigate(self.page_name, self.request_data_callback())