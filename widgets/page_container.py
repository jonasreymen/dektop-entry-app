from models.page_config import PageConfig
from utils.gui.page_builder_factory import PageBuilderFactory
from utils.gui.page_navigator import PageNavigator
from utils.gui.page_navigator_interface import PageNavigatorInterface
from widgets.page import Page

import tkinter as tk

class PageContainer(tk.Tk):
    def __init__(self, page_configurations: list[PageConfig]) -> None:
        super().__init__()
        
        self.minsize(width=1100, height=500)

        self.title("desktop entry")
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.page_navigator: PageNavigatorInterface = PageNavigator()
        self.page_builder_factory: PageBuilderFactory = PageBuilderFactory(self.page_navigator)
        self.build_pages(page_configurations)

    def build_pages(self, page_configurations: list[PageConfig]) -> list[Page]:
        for page_configuration in page_configurations:
            page = Page(
                self,
                page_configuration.name,
                PageBuilderFactory(self.page_navigator).build(page_configuration.name)
            )
            
            self.page_navigator.register(page)