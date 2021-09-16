from Wall import Wall


class Hexagon():
    def __init__(self, address):
        self.address = address
        self.walls = [Wall(address, i) for i in range (1, 5)]
    
    def get_walls():
        pass
        # return self.walls