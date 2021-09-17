import Book
import py_babel_library
import requests


class Shelf():
    def __init__(self, hex, wall, shelf_num):
        from py_babel_library import BabelClient

        self.hex  = hex
        self.wall = wall
        self.shelf_num = shelf_num
        self.client = BabelClient()
        self._books = None
    
    def init_books(self):
        if not self.client.check_valid_format(self.hex):
            raise ValueError(f"Hexagon format {self.hex} invalid")
            
        if not self.client.check_in_bounds(self.wall, self.shelf_num, 1, 1):
            raise ValueError("Arguments not in bounds")
        
        url = "https://libraryofbabel.info/titler.cgi"
        
        data = {
        'hex': str(self.hex),
        'wall': str(self.wall),
        'shelf': str(self.shelf_num)
        }

        headers = {
            'pragma': 'no-cache',
            'cache-control': 'no-cache'
        }


        r = requests.post('https://libraryofbabel.info/titler.cgi', headers=headers, data=data)
        titles = r.text.split(";")
        return [Book.Book(self.hex, int(self.wall), int(self.shelf_num), i, titles[i-1]) for i in range(1, 33)]

    def get_books(self):
        if self._books is None:
            self._books = self.init_books()
        return self._books.copy()