class Command:
    def __init__(self, name, T):
        self.name = name
        self.T = T

class Schedule:
    def __init__(self):
        self.i = -1
        self.commands = []

    @property
    def E(self) -> int:
        return len(self.commands)

    def add_command(self, command: Command):
        self.commands.append(command)