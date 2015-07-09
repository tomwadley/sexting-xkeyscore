from ..lib.transformer import Transformer
from ..lib.instruction import Instruction
import csv, os
from LatLon import LatLon

# Tube station data from http://commons.wikimedia.org/wiki/London_Underground_geographic_maps/CSV
class TubeData:

    def __init__(self):
        self.__import_stations()

    def is_valid_station(self, station):
        return station in self._stations

    def all_stations(self):
        return sorted(self._stations.keys())

    def nearest_stations(self, station, qty):
        if not self.is_valid_station(station):
            raise Exception('Not a valid station: ' + station)

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

