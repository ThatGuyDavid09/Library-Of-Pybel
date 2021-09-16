import Wall

class Hexagon():
    def __init__(self, address):
        self.address = address
        self._walls = [Wall(address, i) for i in range (1, 5)]

    def get_walls(self):
        return self._walls