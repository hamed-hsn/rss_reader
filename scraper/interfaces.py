from abc import ABCMeta, abstractmethod, abstractproperty


class InterfaceScraper(metaclass=ABCMeta):

    __METHODS__ = ('scrape')

    # @classmethod
    # def __subclasshook__(cls, subclass):
    #     for method in cls.__METHODS__:
    #         if not (hasattr(subclass, method) and callable(getattr(subclass, method))):
    #             return False
    #     return True

    @abstractmethod
    def scrape(self):
        raise NotImplementedError('[-] Not implemented yet!')

    @abstractproperty
    def items(self):
        raise NotImplementedError('[-] Not implemented yet!')
