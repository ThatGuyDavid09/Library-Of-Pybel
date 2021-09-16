from Book import Book
from Page import Page
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import re
import pyperclip


# TODO add type annotations
class BabelClient():
    def get_onclick_and_return_parsed(self, a):
        return a.get("onclick").replace("postform(", "").replace(")", "").replace("'", "").split(",")


    # Ensure passed string is only lowercase letters or numbers, the format the website accepts
    def check_valid_format(self, string):
        return bool(re.match("^[\da-z]+$", string))

    def check_in_bounds(self, wall, shelf, volume, page):
        return 1 <= int(wall) <= 4 and 1 <= int(shelf) <= 5 and 1 <= int(volume) <= 32 and 1 <= int(page) <= 410

    def get_page(self, h, wall, shelf, v, page):
        hexagon = h.lower()
        
        if int(v) <= 9:
            volume = "0" + v

        if not self.check_valid_format(hexagon):
            raise ValueError("Hexagon format invalid")
            
        if not self.check_in_bounds(wall, shelf, volume, page):
            raise ValueError("Arguments not in bounds")

        url = "https://libraryofbabel.info/book.cgi"
        data = {"hex": str(hexagon), 
            "wall": str(wall), 
            "shelf": str(shelf),
            "volume": str(volume),
            "page": str(page)
        }

        r = requests.post(url, data=data)
        page_soup = BeautifulSoup(r.text, "html.parser")
        text = page_soup.find("pre", {"id": "textblock"})
        return Page(hexagon, int(wall), int(shelf), int(volume), int(page), text)
    
    def get_books(self, h, wall, shelf):
        hexagon = h.lower()

        if not self.check_valid_format(hexagon):
            raise ValueError("Hexagon format invalid")
            
        if not self.check_in_bounds(wall, shelf, volume, 1):
            raise ValueError("Arguments not in bounds")
        
        url = "https://libraryofbabel.info/titler.cgi"
        
        data = {
        'hex': str(hexagon),
        'wall': str(wall),
        'shelf': str(shelf)
        }

        r = requests.post('https://libraryofbabel.info/titler.cgi', data=data)
        titles = r.text.split(";")
        return [Book(hexagon, int(wall), int(shelf), i, titles[i-1]) for i in range(1, 33)]



    def search_raw(self, query):
        data = {
            'find': query,
            'btnSubmit': 'Search',
            'method': 'x'
        }

        r = requests.post('https://libraryofbabel.info/search.cgi', data=data)
        return r.text

    def search_exact(self, query):
        data = {
        'find': query,
        'btnSubmit': 'Search',
        'method': 'x'
        }

        r = requests.post('https://libraryofbabel.info/search.cgi', data=data)
        soup = BeautifulSoup(r.text, 'html.parser')

        all_a = soup.find_all("a")
        exact_args = self.get_onclick_and_return_parsed(all_a[0])
        return self.get_page(exact_args[0], exact_args[1], exact_args[2], exact_args[3], exact_args[4])