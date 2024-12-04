from builder.page_builder import PageBuilder
from typeguard import typechecked

@typechecked
class PageConfig:
    def __init__(self, name: str, page_builder: PageBuilder):
        self.name = name
        self.page_builder = page_builder