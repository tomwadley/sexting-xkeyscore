
class Contact:

    def __init__(self, data):
        self._data = data
        self._busy_funcs = {}
        self._state = {}

    def has(self, key):
        return key in self._data

    def get(self, key):
        return self._data[key]

    def is_busy(self, clock):
        for key in self._busy_funcs:
            if self._busy_funcs[key](clock):
                return True
        return False

    def set_busy_func(self, key, func):
        self._busy_funcs[key] = func

    def has_state(self, key):
        return key in self._state

    def get_state(self, key):
        return self._state[key]

    def set_state(self, key, value):
        self._state[key] = value
