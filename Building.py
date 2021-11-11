import json
from Elevators import Elevators


class Building:
    def __init__(self, file_name):
        with open(file_name, "r") as fp:
            di = json.load(fp)
            self._minFloor = int(di["_minFloor"])
            self._maxFloor = int(di["_maxFloor"])
            self._elevators = [Elevators(d) for d in di["_elevators"]]
            # for k in di["_elevators"]:
            #     self._elevators.append(Elevators(k))
    
