import json
from Elevators import Elevators


class Building:
    def __init__(self):
          self._minFloor = 0
          self._maxFloor = 10
          self._elevators = [Elevators(), Elevators(), Elevators]
          print("hello")
    def __init__(self, file_name):
          self.from_json(self, file_name)
          
    def from_json(self,file_name):
        with open(file_name,"r") as fp:
            di=json.load(fp)
            self._minFloor=di["_minFloor"]
            self._maxFloor=di["_maxFloor"]
            self._elevators=di["_elevators"]
