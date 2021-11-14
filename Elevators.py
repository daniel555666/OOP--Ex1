from CallForElevator import CallForElevator
class Elevators:
    def __init__(self, di):
        self.id = int(di["_id"])
        self.speed = float(di["_speed"])
        self.minFloor = int(di["_minFloor"])
        self.maxFloor = int(di["_maxFloor"])
        self.closeTime = float(di["_closeTime"])
        self.openTime = float(di["_openTime"])
        self.startTime = float(di["_startTime"])
        self.stopTime = float(di["_stopTime"])
        self.finalFloor = 0
        self.endTime= float(0)
        
    def timeForCall(self, call) -> float:
        range = abs(self._currentFloor - call.src) + abs(call.src - call.dest)
        timeExtra=2*self._stopTime+self._startTime + 2*self._openTime + 2*self._closeTime
        if self._currentFloor != call.src:
            timeExtra += self._startTime
        return range/self._speed +timeExtra
    
    def isState(self, time) -> bool:
        if self.endTime==0 :
            return True
        return (float(time) >= max(self._endTime.values()))
    
    def addCall(self, c):
        self.finalFloor = c.dest
        self.endTime += timeForCall(c)