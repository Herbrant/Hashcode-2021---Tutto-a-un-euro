class Car:
    def __init__(self):
        self.P = -1
        self.targets = []

        self.id = -1

    def add_target(self, street: str):
        self.targets.append(street)

    def __str__(self) -> str:
        return f"[{self.id}] Targets ({self.P}): {self.targets}"