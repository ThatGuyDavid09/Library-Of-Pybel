import Hexagon
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
        return bool(re.match("^[\da-z]+$", str(string)))

    def check_in_bounds(self, wall, shelf, volume, page):
        return 1 <= int(wall) <= 4 and 1 <= int(shelf) <= 5 and 1 <= int(volume) <= 32 and 1 <= int(page) <= 410

    def get_hexagon(self, h):
        hexagon = h.lower()
        if not self.check_valid_format(hexagon):
            raise ValueError(f"Hexagon format {hexagon} invalid")
        
        return Hexagon.Hexagon(h)
    
    def get_wall(self, h, wall):
        return self.get_hexagon(h).get_walls()[wall - 1]
    
    def get_shelf(self, h, wall, shelf):
        return self.get_hexagon(h).get_walls()[wall - 1].get_shelves()[shelf - 1]

    def get_book(self, h, wall, shelf, volume):
        return self.get_hexagon(h).get_walls()[wall - 1].get_shelves()[shelf - 1].get_books()[volume - 1]

    def get_page(self, h, wall, shelf, v, page):
        return self.get_hexagon(h).get_walls()[wall - 1].get_shelves()[shelf - 1].get_books()[v - 1].get_pages()[page - 1]
        
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

def main():
    client = BabelClient()
    # page = client.get_page("12", 2, 3, 10, 123)
    # print(page.get_content())
    content = client.get_page("123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123123", 1, 2, 3, 4).get_content()
    #print(content)
    pyperclip.copy(content)

if __name__ == "__main__":
    main()