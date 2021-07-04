from abc import ABC, abstractmethod
from typing import Dict, Union
from scraper.interfaces import InterfaceScraper
from errors import ReadOnlyAttrError


class BaseScraper(InterfaceScraper, ABC):

    def __init__(self, content:Union[str, bytes], pattern:Dict) -> None:
        self._content = content
        self._pattern = pattern
    
    @abstractmethod
    def scrape(self):
        raise NotImplementedError('[-] Not implemented yet!')
    
    @property
    def data(self):
        raise NotImplementedError('[-] Not implemented yet!')
    
    @data.setter
    def data(self, v):
        raise ReadOnlyAttrError('[-] data attr is readonly')
