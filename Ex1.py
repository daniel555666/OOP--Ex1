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
        "buildingName": "input\Ex1_input\Ex1_Buildings\B1.json",
        "callsName": "input\Ex1_input\Ex1_Calls\Calls_a.csv",
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
        #print(data)
        for k in data:
            if (int(k[2]) >= building._minFloor and int(k[2]) <= building._maxFloor) and (int(k[3]) >= building._minFloor and int(k[3]) <= building._maxFloor):
                calls.append(CallForElevator(k))
    return calls


def writeCalls():
    dataCalls = []
    for k in calls:
        dataCalls.append(k.__dict__.values())
    with open(myinput["outputName"], 'w', newline="") as fu:
        csvwriter = csv.writer(fu)
        csvwriter.writerows(dataCalls)


def allRestElevators(time):
    list = []
    for e in building._elevators:
        if e.isState(time):
            list.append(e)
    return list

def timeToSrc(elev, call):
    if(elev._currentFloor == call.src):
        return 0
    length = abs(elev._currentFloor-call.src)
    return length/elev._speed + elev._startTime+elev._stopTime

def chooseElevator():
    for c in calls:
        # restElevators = allRestElevators(c.time)
        # # we need to check if restElevators not Empty
        # fastestE = restElevators[0]
        # fastestTime = timeToSrc(restElevators[0], c)
        # for e in restElevators:
        #     temp = timeToSrc(e, c)
        #     if temp < fastestTime:
        #         fastestE = e
        #         fastestTime = temp
        # c.elevator = fastestE._id
        # fastestE._endTime.update({c: fastestE.timeForCall(c)})
        c.elevator = random.randint(0, len(building._elevators)-1)
def runTester():
    subprocess.Popen(["powershell.exe", "java -jar lib\Ex1_checker_V1.2_obf.jar 1111,2222,3333 "+ myinput["buildingName"] +"  "+ myinput["outputName"] +"  out.log"])

if __name__ == "__main__":
    myinput = inputs()
    building = Building(myinput["buildingName"])
    calls = readCalls(myinput["callsName"])
    chooseElevator()
    writeCalls()
    runTester()
