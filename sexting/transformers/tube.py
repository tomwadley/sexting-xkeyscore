from ..lib.transformer import Transformer
import csv, os
from LatLon import LatLon
import utils

# Tube station data from http://commons.wikimedia.org/wiki/London_Underground_geographic_maps/CSV
class Tube(Transformer):

    __punctuation_characters = ['.', ',', '?', '!', ';', ':', '-']

    def __init__(self):
        self.__import_stations()

    def can_handle_character(self, character):
        return character in Tube.__punctuation_characters

    def can_handle_contact(self, contact):
        return contact.has('tubestation')

    def num_required_contacts(self):
        return 1

    def transform(self, character, contacts, clock):
        contact = contacts[0]
        station = contact.get('tubestation')
        stations = self.__nearest_stations(station, len(Tube.__punctuation_characters))
        index = Tube.__punctuation_characters.index(character)
        destination = stations[index]

        return 'Character: {0}, At: {1}, Begin tube journey by: {2}, From: {3}, To: {4}'.format(character, clock.block_range_str(), contact.get('name'), station, destination)

    def __nearest_stations(self, station, qty):
        point1 = self._stations[station]
        distances = {}

        for name in self._stations:
            if name == station:
                continue

            point2 = self._stations[name]
            distance = point1.distance(point2)
            distances[name] = distance

        nearest_stations = sorted(distances, lambda n1, n2: cmp(distances[n1], distances[n2]))
        return nearest_stations[:qty]

    def __import_stations(self):
        self._stations = {}

        with open(os.path.join('resources', 'tube.csv'), 'r') as csvfile:
            rows = csv.reader(csvfile)

            next(rows)
            for row in rows:
                name = row[3]
                lat = float(row[1])
                lng = float(row[2])

                self._stations[name] = LatLon(lat, lng)

