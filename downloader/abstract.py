from abc import ABC, abstractmethod
from errors import ReadOnlyAttrError, DownloadMethodNotCallError


class AbstractDownloader(ABC):
    #
    # ────────────────────────────────────────────────  ──────────
    #  abstract downlader:
    #       this class must get an url and download it!
    # ──────────────────────────────────────────────────────────
    #
    DOWNLOADER_NOT_SET_STATUS_CODE = -1
    DOWNLOADER_NOT_SET_TEXT = 'BAD'

    def __init__(self, url):
        self.url = url
        self._text = self.DOWNLOADER_NOT_SET_TEXT
        self._status_code = self.DOWNLOADER_NOT_SET_STATUS_CODE

    @property
    def url(self):
        return self._url
    
    @url.setter
    def url(self, v):
        assert isinstance(v, str)
        assert v.lower().startswith('http')
        self._url = v

    @abstractmethod
    def download(self):
        raise NotImplementedError('[-] Not implemented yet!')

    @property
    def status_code(self):
        if self._status_code == self.DOWNLOADER_NOT_SET_STATUS_CODE:
            raise DownloadMethodNotCallError('download method not called!')
        return self._status_code

    @status_code.setter
    def status_code(self, v):
        raise ReadOnlyAttrError('[-] status-code attribute is readOnly!')
    
    @property    
    def text(self):
        if self._text == self.DOWNLOADER_NOT_SET_TEXT:
            raise DownloadMethodNotCallError('download method not called!')
        return self._text

    @text.setter
    def text(self, v):
        raise ReadOnlyAttrError('[-] text attribute is readOnly!')
