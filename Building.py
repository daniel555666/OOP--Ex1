from Elevators import Elevators


class Building:
    def __init__(self):
        self._minFloor = 0
        self._maxFloor = 10
        self._elevators = [Elevators(), Elevators(), Elevators]
        print("hello")
    def __print(self):
        print("hello")