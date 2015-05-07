
class Instruction(object):

    def __init__(self, medium, character, clock, contact, data = {}):
        self._medium = medium
        self._character = character
        self._clock = clock
        self._contact = contact
        self._data = data

    def medium(self):
        return self._medium

    def character(self):
        return self._character

    def clock(self):
        return self._clock

    def contact(self):
        return self._contact

    def data(self, key):
        return self._data[key]

    def __str__(self):
        data = ', '.join(map(lambda k: "{0}: {1}".format(k, self._data[k]), self._data))
        return "For: '{0}', at {1}, {2}, should {3} ({4})".format(self._character, self._clock.block_range_str(), self._contact.get('name'), self._medium, data)

