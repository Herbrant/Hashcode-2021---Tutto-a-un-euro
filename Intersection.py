class Intersection:
    def __init__(self) -> None:
        self.streets = []
        self.id = None

    def add_street(self, street):
        self.streets.append(street)
    