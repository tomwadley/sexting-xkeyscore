
class Contact:

    def __init__(self, name, data):
        self._name = name
        self._data = data
        self._busy_funcs = {}
        self._state = {}

    def name(self):
        return self._name

    def has(self, key):
        if key == 'name':
            return True
        return key in self._data

    def get(self, key):
        if key == 'name':
            return self._name
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

    def __str__(self):
        return self._name
