from py_babel_library import BabelClient
from Page import Page


class Book():
    def __init__(self, hex, wall, shelf, book_num, title):
        self.hex = hex
        self.wall = wall
        self.shelf = shelf
        self.title = title
        self.book_num = book_num
        self.client = BabelClient()
        self._pages = [Page(hex, wall, shelf, book_num, i, self.client.get_page(hex, wall, shelf, book_num, i)) for i in range(1, 411)]
    
    def get_pages(self):
        return self._pages.copy()
