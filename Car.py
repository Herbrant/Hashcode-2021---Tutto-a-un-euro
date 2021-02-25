class Car:
    def __init__(self):
        self.P = -1
        self.targets = []

    def add_target(self, street: str):
        self.targets.append(street)

    def __str__(self) -> str:
        return f"Targets ({self.P}): {self.targets}"