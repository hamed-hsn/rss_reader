from typing import Dict, Union
from bs4 import BeautifulSoup
from scraper.abstracts import BaseScraper
from scraper.item import ItemScraped
from errors import ReadOnlyAttrError


class CommonScraper(BaseScraper):

    def __init__(self, content: Union[str, bytes], pattern: Dict):
        super().__init__(content, pattern)
        self._items = None
    
    def addItem(self, key, val):
        if not self._items:
            self._items = []
        item = ItemScraped()
        item.set(key, val)
        self._items.append(item)

    @property
    def items(self):
        return self._items
    
    @items.setter
    def items(self, v):
        raise ReadOnlyAttrError("[-] items attr is readonly")

    def scrape(self):        
        soup = BeautifulSoup(self._content, 'lxml')
        for k, v in self._pattern.items():
            print(f'[+] scrape {k}')
            self.addItem(k, soup.select(v))
