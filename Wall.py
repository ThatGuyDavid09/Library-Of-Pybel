import Shelf


class Wall():
    def __init__(self, hex, wall_num):
        self.hex = hex
        self.wall_num = wall_num
        self._shelves = None
    
    def get_shelves(self):
        if self._shelves  is None:
            self._shelves = [Shelf.Shelf(self.hex, self.wall_num, i) for i in range(1, 6)]
        return self._shelves