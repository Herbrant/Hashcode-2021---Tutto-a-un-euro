class Street:
    def __init__(self) -> None:
        self.B = -1
        self.E = -1
        self.name = None
        self.L = -1

        self.passing_cars = []

        self.interested_cars = 0

    def add_car(self, car):
        self.passing_cars.append(car)

    def remove_car(self, car):
        self.passing_cars.remove(car)

    def __str__(self) -> str:
        passing_cars_str = [car.id for car in self.passing_cars]
        return f"Begin intersection: {self.B}\nEnd intersection: {self.E}\nName: {self.name}\nLength: {self.L}\nPassing cars: {passing_cars_str}"