class Street:
    def __init__(self) -> None:
        self.B = -1
        self.E = -1
        self.name = None
        self.L = -1

    def __str__(self) -> str:
        return f"Begin intersection: {self.B}\nEnd intersection: {self.E}\nName: {self.name}\nLength: {self.L}"