class Page():
    def __init__(self, hex, wall, shelf, book, page_num, content):
        self.hex = hex
        self.wall = wall
        self.shelf = shelf
        self.book = book
        self.page_num = page_num
        self._content = content
    
    def get_content(self):
        return self._content