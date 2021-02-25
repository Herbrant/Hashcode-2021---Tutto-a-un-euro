class State:
    def __init__(self):
        self.D = -1
        self.I = -1
        self.S = -1
        self.V = -1
        self.F = -1

    def __str__(self) -> str:
        return f"Duration: {self.D}\nNumber of intersections: {self.I}\nNumber of streets: {self.S}\nNumber of cars: {self.V}\nBonus points: {self.F}"