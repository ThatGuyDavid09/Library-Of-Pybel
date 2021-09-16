import Shelf


class Wall():
    def __init__(self, hex, wall_num):
        self.hex = hex
        self.wall_num = wall_num
        self._shelves = [Shelf.Shelf(hex, wall_num, i) for i in range(1, 6)]
    
    def get_shelves(self):
        return self._shelves