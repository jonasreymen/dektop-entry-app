from builder.add_desktop_entry_page_builder import AddDesktopEntryPageBuilder
from builder.edit_desktop_entry_page_builder import EditDesktopEntryPageBuilder
from builder.list_desktop_entries_page_builder import ListDesktopEntriesPageBuilder
from builder.page_builder import PageBuilder
from enums.page import Page
from utils.gui.page_navigator_interface import PageNavigatorInterface

class PageBuilderFactory:
    def __init__(self, page_navigator: PageNavigatorInterface) -> None:
        self.page_navigator: PageNavigatorInterface = page_navigator
    
    def build(self, page_name: str) -> PageBuilder:
        match page_name:
            case Page.LIST_PAGE.value:
                return ListDesktopEntriesPageBuilder(self.page_navigator)
            case Page.ADD_PAGE.value:
                return AddDesktopEntryPageBuilder(self.page_navigator)
            case Page.EDIT_PAGE.value:
                return EditDesktopEntryPageBuilder(self.page_navigator)