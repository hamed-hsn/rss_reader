from downloader.abstract import AbstractDownloader
import requests
from typing import Dict, Tuple, Union
from requests_html import HTMLSession


class CommonDownloader(AbstractDownloader):
    
    def __init__(self, url):
        super().__init__(url)    

    def download(self):
        print(f'[+] download link : {self.url}')
        res = requests.get(self.url)
        self._status_code = res.status_code
        self._text = res.text
    
    
class FeaturedDownloader(AbstractDownloader):

    def __init__(self, url, timeout:Tuple[int, int]=(5,15), proxies:Union[None, Dict]=None):
        super().__init__(url)
        self._timeout = timeout
        self._proxies = proxies
        self._text = self.DOWNLOADER_NOT_SET_TEXT
        self._status_code = self.DOWNLOADER_NOT_SET_STATUS_CODE

    def download(self):
        res = requests.get(self.url, timeout=self._timeout, proxies=self._proxies)
        self._status_code = res.status_code
        self._text = res.text
    

class JavaScriptRenderableDownloader(AbstractDownloader):

    def __init__(self, url):
        super().__init__(url)        

    def download(self):
        session = HTMLSession()
        res = session.get(self.url)
        res.html.render()
        self._text = res.html.html
        self._status_code = res.status_code
