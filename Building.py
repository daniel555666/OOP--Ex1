import json
from Elevators import Elevators


class Building:
    def __init__(self, file_name):
        with open(file_name, "r") as fp:
            di = json.load(fp)
            self.minFloor = int(di["_minFloor"])
            self.maxFloor = int(di["_maxFloor"])
            self.elevators = [Elevators(d) for d in di["_elevators"]]
