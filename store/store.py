class Store:
    def __init__(self):
        """
        Short to long URL map
        """
        self.store = {}

    def get(self, short_url: str):
        return self.store.get(short_url)

    def set(self, long_url: str, short_url: str):
        self.store[short_url] = long_url
        return
