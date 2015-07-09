from ..lib.transformer import Transformer
from ..lib.instruction import Instruction
from ..lib.tubedata import TubeData
import csv, os
from LatLon import LatLon

class Tube(Transformer):

    __punctuation_characters = ['.', ',', '?', '!', ';', ':', '-']

    def __init__(self):
        self._tubedata = TubeData()

    def can_handle_character(self, character):
        return character in Tube.__punctuation_characters

    def can_handle_contact(self, contact, clock):
        return contact.has('tubestation')

    def num_required_contacts(self):
        return 1

    def transform(self, character, contacts, clock):
        contact = contacts[0]
        station = contact.get('tubestation')
        if contact.has_state('lasttube'):
            station = contact.get_state('lasttube')

        stations = self._tubedata.nearest_stations(station, len(Tube.__punctuation_characters))
        index = Tube.__punctuation_characters.index(character)
        destination = stations[index]

        contact.set_state('lasttube', destination)
        contact.set_busy_func('tube', lambda clk: clock.jump_forward(12) > clk)

        return Instruction('tube', character, clock, contact, {'from_station': station, 'to_station': destination})

