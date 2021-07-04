from abc import ABCMeta, abstractmethod


class InterfaceRssReader(metaclass=ABCMeta):

    __METHODS__ = ('download', 'parse', 'scrape', 'run')

    # @classmethod
    # def __subclasshook__(cls, subclass):
    #     for method in cls.__METHODS__:
    #         if not (hasattr(subclass, method) and callable(getattr(subclass, method))):
    #             return False
    #     return True

    @abstractmethod
    def scrape(self, items):
        raise NotImplementedError('[-] Not implemented yet!')
    
    @abstractmethod
    def parse(self):
        raise NotImplementedError('[-] Not implemented yet!')

    @abstractmethod
    def download(self, links:list):
        raise NotImplementedError('[-] Not implemented yet!')

    @abstractmethod
    def run(self):
        raise NotImplementedError('[-] Not implemented yet!')
