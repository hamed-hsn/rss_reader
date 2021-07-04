from abc import ABC
from typing import Dict
from rss.interfaces import InterfaceRssReader
from scraper.interfaces import InterfaceScraper
from downloader.abstract import AbstractDownloader
from typing import final


class BaseRssReader(InterfaceRssReader, ABC):

    def __init__(self, rsslink:str, downloaderClass:AbstractDownloader, scraperClass:InterfaceScraper, pattern:Dict):
        self._rsslink = rsslink
        assert issubclass(downloaderClass, AbstractDownloader)
        self._downloadrClass = downloaderClass
        self._pattern = pattern
        assert issubclass(scraperClass, InterfaceScraper)
        self._scraperClass = scraperClass
    
    @property
    def scraperClass(self):
        return self._scraperClass

    @property
    def downloaderClass(self):
        return self._downloadrClass
    
    @property
    def rsslink(self):
        return self._rsslink
    
    @property
    def pattern(self):
        return self._pattern

    @final
    def run(self):
        links = self.parse()
        items = self.download(links)
        self.scrape(items)
    
