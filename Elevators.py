from CallForElevator import CallForElevator
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
        self._endTime={CallForElevator(0,0,0,0):0}
        
    def timeForCall(self, call):
        range = abs(self._currentFloor - call.src) + abs(call.src - call.dest)
        timeExtra=2*self._stopTime+self._startTime + 2*self._openTime + 2*self._closeTime
        if self._currentFloor != call.src:
            timeExtra += self._startTime
        return range/self._speed +timeExtra
    
    def isState(self, time):
        if self._endTime.__len__==0 :
            return True
        print(self._endTime.values().__dict__)
        return (time >= max(self._endTime.values()))
        