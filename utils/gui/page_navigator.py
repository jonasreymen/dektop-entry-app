from utils.gui.page_navigator_interface import PageNavigatorInterface
from widgets.page import Page

class PageNavigator(PageNavigatorInterface):
    pages: dict[str, Page] = {}
    
    def __init__(self, pages: list["Page"] = []) -> None:
        self.register_pages(pages)
    
    def register_pages(self, pages: list["Page"] = []) -> None:
        for page in pages:
            self.register(page)
    
    def register(self, page: "Page") -> None:
        self.pages[page.name] = page
    
    def navigate(self, name: str, request_data: dict = {}) -> None:
        """ opens a specific page """
        self.pages[name].load(request_data)