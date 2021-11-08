class Elevators:
    def __init__(self, di):
        self._id = di["_id"]
        self._speed = di["_speed"]
        self._minFloor = di["_minFloor"]
        self._maxFloor = di["_maxFloor"]
        self._closeTime = di["_closeTime"]
        self._openTime = di["_openTime"]
        self._startTime = di["_startTime"]
        self._stopTime = di["_stopTime"]
        self._currentFloor = 0