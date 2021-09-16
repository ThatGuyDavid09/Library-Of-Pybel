import Book
import py_babel_library
import requests


class Shelf():
    def __init__(self, hex, wall, shelf_num):
        from py_babel_library import BabelClient
        from Book import Book

        self.hex  = hex
        self.wall = wall
        self.shelf_num = shelf_num
        self.client = BabelClient()
        self._books = self.client.get_books(hex, wall, shelf_num)
    
    def init_books(self):
        if not self.client.check_valid_format(self.hex):
            raise ValueError("Hexagon format invalid")
            
        if not self.client.check_in_bounds(self.wall, self.shelf_num, 1, 1):
            raise ValueError("Arguments not in bounds")
        
        url = "https://libraryofbabel.info/titler.cgi"
        
        data = {
        'hex': str(self.hex),
        'wall': str(self.wall),
        'shelf': str(self.shelf)
        }

        r = requests.post('https://libraryofbabel.info/titler.cgi', data=data)
        titles = r.text.split(";")
        return [Book(self.hex, int(self.wall), int(self.shelf), i, titles[i-1]) for i in range(1, 33)]

    def get_books(self):
        return self._books.copy()