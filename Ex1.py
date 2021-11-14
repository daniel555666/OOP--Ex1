import sys
from CallForElevator import CallForElevator
from Building import Building
from Elevators import Elevators
import csv
import random
import subprocess


def inputs():
    if len(sys.argv) == 1:
        di = {
            "buildingName": "input\Ex1_Buildings\B1.json",
            "callsName": "input\Ex1_Calls\Calls_a.csv",
            "outputName": "out.csv"
        }
    else:
        di = {
            "buildingName": sys.argv[1],
            "callsName": sys.argv[2],
            "outputName": sys.argv[3]
        }
    return di


def readCalls(file_name):
    calls = []
    with open(file_name) as fp:
        data = csv.reader(fp)
        # print(data)
        for k in data:
            if (int(k[2]) >= building.minFloor and int(k[2]) <= building.maxFloor) and (int(k[3]) >= building.minFloor and int(k[3]) <= building.maxFloor):
                calls.append(CallForElevator(k))
    return calls


def writeCalls():
    dataCalls = []
    for k in calls:
        dataCalls.append(k.__dict__.values())
    with open(myinput["outputName"], 'w', newline="") as fu:
        csvwriter = csv.writer(fu)
        csvwriter.writerows(dataCalls)


def allRestElevators(time) -> list:
    list = []
    for e in building.elevators:
        if e.isState(time):
            list.append(e)
    return list


def timeToSrc(elev, call):
    if(elev.finalFloor == call.src):
        return 0
    length = abs(elev.finalFloor - call.src)
    return length/elev.speed + elev.startTime+elev.stopTime


def chooseElevator():
    for c in calls:
        if c.isDone() == False:
            elev = allocate(c)
            c.elevator = elev.index
            for c2 in calls:
                if elev.endTime + timeToSrc(elev, c2) < c2.time and c.src < c2.src and c.dest > c2.dest:
                    c2.elevator = elev.index
                    elev.endTime += elev.extraTime()  # startstopopenclose

        elev.addCall(c)


def allocate(c):
    ans = building.elevators[0]
    rests = allRestElevators(c.time)
    if len(rests) != 0:
        minE = rests[0]
        minTime = timeToSrc(minE, c)
        for e in rests:
            tempTime = timeToSrc(e, c)
            if(tempTime < minTime):
                minE = e
                minTime = tempTime
        ans = minE
    else:
        minE = building.elevators[0]
        minR = timeToSrc(minE, c)
        for e in building.elevators:
            tempTime = timeToSrc(e, c)
            if(tempTime < minR):
                minE = e
                minR = tempTime
        ans = minE
    return ans


def runTester():
    subprocess.Popen(["powershell.exe", "java -jar lib\Ex1_checker_V1.2_obf.jar 1111,2222,3333 " +
                     myinput["buildingName"] + "  " + myinput["outputName"] + "  outputFormTEster.log"])


if __name__ == "__main__":
    myinput = inputs()
    building = Building(myinput["buildingName"])
    calls = readCalls(myinput["callsName"])
    chooseElevator()
    writeCalls()
    runTester()
