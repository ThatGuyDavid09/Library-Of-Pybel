import py_babel_library
import requests
from bs4 import BeautifulSoup

class Page():
    def __init__(self, hex, wall, shelf, book, page_num):
        from py_babel_library import BabelClient

        self.hex = hex
        self.wall = wall
        self.shelf = shelf
        self.book = book
        self.page_num = page_num
        self.client = BabelClient()
        self._content = self.init_content()

    def init_content(self):
        hexagon = self.lower()
        volume = self.book

        if int(volume) <= 9:
            volume = "0" + volume

        if not self.client.check_valid_format(hexagon):
            raise ValueError("Hexagon format invalid")
            
        if not self.client.check_in_bounds(self.wall, self.shelf, volume, self.page_num):
            raise ValueError("Arguments not in bounds")

        url = "https://libraryofbabel.info/book.cgi"
        data = {"hex": str(hexagon), 
            "wall": str(self.wall), 
            "shelf": str(self.shelf),
            "volume": str(volume),
            "page": str(self.page_num)
        }

        r = requests.post(url, data=data)
        page_soup = BeautifulSoup(r.text, "html.parser")
        text = page_soup.find("pre", {"id": "textblock"})
        return text
    
    def get_content(self):
        return self._content