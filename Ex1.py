from CallForElevator import CallForElevator
from Building import Building
from Elevators import Elevators
import csv
import random


def readCalls(file_name):
    calls = []
    with open(file_name) as fp:
        data = csv.reader(fp)
        for k in data:
            if (int(k[2]) >= building._minFloor and int(k[2]) <= building._maxFloor) and (int(k[3]) >= building._minFloor and int(k[3]) <= building._maxFloor):
                calls.append(CallForElevator(k))
    return calls


def writeCalls():
    dataCalls = []
    for k in calls:
        dataCalls.append(k.__dict__.values())
    with open("output.csv", 'w', newline="") as fu:
        csvwriter = csv.writer(fu)
        csvwriter.writerows(dataCalls)


def allRestElevators(time):
    list = []
    for e in building._elevators:
        if e.isState(time):
            list.append(e)
    return list


def chooseElevator():
    for c in calls:
        restElevators = allRestElevators(c.time)
        # we need to check if restElevators not Empty
        fastestE = restElevators[0]
        fastestTime = timeToSrc(restElevators[0], c)
        for e in restElevators:
            temp = timeToSrc(e, c)
            if temp < fastestTime:
                fastestE = e
                fastestTime = temp
        c.elevator = fastestE._id
        fastestE.endTime.update({c: fastestE.timeForCall(c)})


def timeToSrc(elev, call):
    if(elev._currentFloor == call.src):
        return 0
    length = abs(elev._currentFloor-call.src)
    return length/elev._speed + elev._startTime+elev._stopTime


if __name__ == "__main__":
    building = Building("input\Ex1_input\Ex1_Buildings\B1.json")
    calls = readCalls("input\Ex1_input\Ex1_Calls\Calls_d.csv")
    chooseElevator()
    writeCalls()
    print(building._elevators[0].__dict__)
    print(calls[0].__dict__)
