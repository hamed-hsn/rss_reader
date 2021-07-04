from typing import Dict
from downloader.abstract import AbstractDownloader
from rss.abstracts import BaseRssReader
from feedparser import parse
from scraper.interfaces import InterfaceScraper


class CommonRssReader(BaseRssReader):

    def __init__(self, rsslink: str, downloaderClass: AbstractDownloader, scraperClass: InterfaceScraper, pattern: Dict):
        super().__init__(rsslink, downloaderClass, scraperClass, pattern)
        self._data = None
    
    @property
    def data(self):
        return self._data
    
    def addData(self, item):
        if not self._data:
            self._data = []
        self._data.append(item)
    
    def parse(self):
        _parser = parse(self.rsslink)
        _links = []
        _entrise = _parser.entries
        if _entrise:
            _links = [l.link for l in _entrise]
        return _links
    
    def download(self, links: list):
        items = []
        for link in links:
            d:AbstractDownloader = self.downloaderClass(link)
            d.download()
            items.append(d.text)
        return items
    
    def scrape(self, items):
        for item in items:
            s:InterfaceScraper = self.scraperClass(item, self.pattern)
            s.scrape()
            self.addData(s.items)

