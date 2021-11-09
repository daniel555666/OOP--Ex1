from CallForElevator import CallForElevator
from Building import Building
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

#choose random elevator 
def chooseElevator():
    for k in calls:
        k.elevator = random.randint(0, len(building._elevators) - 1)


if __name__ == "__main__":
    building = Building("input\Ex1_input\Ex1_Buildings\B1.json")
    calls = readCalls("input\Ex1_input\Ex1_Calls\Calls_d.csv")
    chooseElevator()
    writeCalls()
    print(building._elevators[0].__dict__)
    print(calls[0].__dict__)
