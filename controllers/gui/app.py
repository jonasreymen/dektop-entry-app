from builder.add_desktop_entry_page_builder import AddDesktopEntryPageBuilder
from builder.list_desktop_entries_page_builder import ListDesktopEntriesPageBuilder
from widgets.page_container import PageContainer
from enums.page import Page
from models.page_config import PageConfig

def run_gui() -> None:
    app = PageContainer(get_page_configurations())
    
    app.navigator.navigate(Page.LIST_PAGE.value)
    
    app.mainloop()

def get_page_configurations() -> list[PageConfig]:
    return [
        PageConfig(Page.LIST_PAGE.value, ListDesktopEntriesPageBuilder()),
        PageConfig(Page.ADD_PAGE.value, AddDesktopEntryPageBuilder())
    ]