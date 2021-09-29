from pprint import pprint
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
        self._content = None

    def init_content(self):
        hexagon = self.hex.lower()
        volume = self.book

        if int(volume) <= 9:
            volume = "0" + str(volume)

        if not self.client.check_valid_format(hexagon):
            raise ValueError("Hexagon format invalid")
            
        if not self.client.check_in_bounds(self.wall, self.shelf, volume, self.page_num):
            raise ValueError("Arguments not in bounds")

        url = "https://libraryofbabel.info/book.cgi"
        data = {"hex": str(hexagon), 
            "wall": str(self.wall), 
            "shelf": str(self.shelf),
            "volume": str(volume),
            "page": str(self.page_num),
            "title": ""
        }

        headers = {
            'pragma': 'no-cache',
            'cache-control': 'no-cache'
        }

        r = requests.post(url, headers=headers, json=data)

        page_soup = BeautifulSoup(r.text, "html.parser")
        text = page_soup.find("pre", {"id": "textblock"})
        return text.text
    
    def get_content(self):
        if self._content is None:
            self._content = self.init_content()
        return self._content
    
    def __str__(self):
        return self.get_content()