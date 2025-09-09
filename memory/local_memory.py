
class LocalMemory:
    def __init__(self):
        self.store = {}

    def save(self, key, value):
        self.store[key] = value

    def retrieve(self, key):
        return self.store.get(key)
