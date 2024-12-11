from dotenv import load_dotenv
from utils.gui.page_navigator import PageNavigator
from widgets.page.add_desktop_entry_page import AddDesktopEntryPage
from widgets.page.desktop_entry_root import DesktopEntryRoot
from enums.page_name import PageName
from widgets.page.edit_desktop_entry_page import EditDesktopEntryPage
from widgets.page.list_desktop_entry_page import ListDesktopEntriesPage
from widgets.page.page import Page

def run_gui() -> None:
    load_dotenv()
    
    root = DesktopEntryRoot()
    navigator = PageNavigator()
    
    navigator.register_pages(generate_pages(root, navigator))
    
    navigator.navigate(PageName.LIST_PAGE.value)
    
    root.mainloop()

def generate_pages(root: DesktopEntryRoot, navigator: PageNavigator) -> list[Page]:
    return [
        ListDesktopEntriesPage(root, navigator),
        AddDesktopEntryPage(root, navigator),
        EditDesktopEntryPage(root, navigator),
    ]