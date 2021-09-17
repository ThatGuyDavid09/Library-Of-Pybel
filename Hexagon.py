import Wall

class Hexagon():
    def __init__(self, address):
        self.address = address
        self._walls = None

    def get_walls(self):
        if self._walls is None:
            self._walls = [Wall.Wall(self.address, i) for i in range (1, 5)]
        return self._walls