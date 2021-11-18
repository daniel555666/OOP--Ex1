from CallForElevator import CallForElevator
from queue import PriorityQueue


class Elevators:
    def __init__(self, di):
        #from json
        self.id = int(di["_id"])
        self.speed = float(di["_speed"])
        self.minFloor = int(di["_minFloor"])
        self.maxFloor = int(di["_maxFloor"])
        self.closeTime = float(di["_closeTime"])
        self.openTime = float(di["_openTime"])
        self.startTime = float(di["_startTime"])
        self.stopTime = float(di["_stopTime"])
        
        self.currentFloor = 0
        self.timeStart= 0 #the time that the elevator can start move
        self.state = 0  # 1 Up, -1 DOWN, 0 LEVEL

        self.destList = PriorityQueue() #all the floor that the elevator go
        self.dest = 0#the current dest

        self.timeStop = self.openTime + self.closeTime + self.startTime + self.stopTime #the time that take the elevator to stop and start

    #do "smart" pop from deatList
    def updetDest(self):
        if not self.destList.empty():
            self.dest = self.state * self.destList.get()
        else:
            self.state = 0
        return self.dest
