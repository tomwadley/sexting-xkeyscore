
class Contact:

    def __init__(self, data):
        self.data = data

    def has(self, key):
        return key in self.data

    def get(self, key):
        return self.data[key]
