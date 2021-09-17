import py_babel_library
import Page


class Book():
    def __init__(self, hex, wall, shelf, book_num, title):
        from py_babel_library import BabelClient

        self.hex = hex
        self.wall = wall
        self.shelf = shelf
        self.title = title
        self.book_num = book_num
        self.client = BabelClient()
        self._pages = None

    def get_pages(self):
        if self._pages is None:
            self._pages = [Page.Page(self.hex, self.wall, self.shelf, self.book_num, i) for i in range(1, 411)]
        return self._pages.copy()
    
    def __str__(self):
        return f"<Book {self.title}>"
