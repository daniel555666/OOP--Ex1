from CallForElevator import CallForElevator
class Elevators:
    def __init__(self, di, index):
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
        self.index = index
        
    def timeForCall(self, call) -> float:
        range = abs(self.finalFloor - call.src) + abs(call.src - call.dest)
        timeExtra=2*self.stopTime+self.startTime + 2*self.openTime + 2*self.closeTime
        if self.finalFloor != call.src:
            timeExtra += self.startTime
        return range/self.speed +timeExtra
    def isState(self, time) -> bool:
        if self.endTime==0 :
            return True
        return (float(time) >= self.endTime)
    def addCall(self, c):
        self.endTime = self.endTime + self.timeForCall(c)
        self.finalFloor = c.dest
        