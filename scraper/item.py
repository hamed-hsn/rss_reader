class ItemScraped:

    def __init__(self):
        self._key = None
        self._data = None

    @property
    def key(self):
        return self._key
    
    @key.setter
    def key(self, v):
        self._key = v

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, v):
        self._data = v

    def set(self, key, val):
        self.key = key
        self.data = val

    def __str__(self) :
        return f'ItemScraped({self._key} : {self._data})'
    
    def __repr__(self):
        return str(self)
        

