import json
from Elevators import Elevators


class Building:
    def __init__(self, file_name):
        with open(file_name, "r") as fp:
            di = json.load(fp)
            self._minFloor = di["_minFloor"]
            self._maxFloor = di["_maxFloor"]
            self._elevators = []
            for k in di["_elevators"]:
                self._elevators.append(Elevators(k))
