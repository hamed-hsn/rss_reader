


class ReadOnlyAttrError(Exception):
    def __init__(self, *args: object):
        super().__init__(*args)


class DownloadMethodNotCallError(Exception):
    def __init__(self, *args: object):
        super().__init__(*args)
