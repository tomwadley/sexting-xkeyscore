
class Contact:

    def __init__(self, data):
        self._data = data
        self._state = {}

    def has(self, key):
        return key in self._data

    def get(self, key):
        return self._data[key]

    def has_state(self, key):
        return key in self._state

    def get_state(self, key):
        return self._state[key]

    def set_state(self, key, value):
        self._state[key] = value
