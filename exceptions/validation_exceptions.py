class ValidationError(Exception):
    def __init__(self, errors: list) -> None:
        super().__init__("Validation error")

        self.errors = errors