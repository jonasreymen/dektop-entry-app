from builder.page_builder import PageBuilder
from typeguard import typechecked

@typechecked
class PageConfig:
    def __init__(self, name: str) -> None:
        self.name = name