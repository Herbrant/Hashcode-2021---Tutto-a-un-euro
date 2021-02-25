class Intersection:
    def __init__(self) -> None:
        self.streets = []
        self.id = None

    def add_street(self, street):
        self.streets.append(street)
    
    def __str__(self) -> str:
        streets_str = [street.name for street in self.streets]
        return f"({self.id}): {streets_str}"