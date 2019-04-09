
class Memory:

    def __init__(self):
        self.map = dict()

    def store(self, key, value):
        self.map[key] = value

    def get(self, key):
        if key not in self.map:
            return None
        return self.map[key]
