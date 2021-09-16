from py_babel_library import BabelClient


class Shelf():
    def __init__(self, hex, wall, shelf_num):
        self.hex  = self.hex
        self.wall = self.wall
        self.shelf_num = shelf_num
        self.client = BabelClient()
        self._books = self.client.get_books(hex, wall, shelf_num)
    
    def get_books(self):
        return self._books.copy()