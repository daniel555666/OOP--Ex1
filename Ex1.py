from Building import Building
import csv
import random

from CallForElevator import CallForElevator
def readCalls(file_name):
    calls = []
    with open(file_name) as fp:
        data = csv.reader(fp)
        for k in data:
            calls.append(CallForElevator(k))
    return calls
def writeCalls():
    dataCalls = []
    for k in calls:
        dataCalls.append(k.__dict__.values())
    with open("output.csv", 'w', newline= "") as fu:
        csvwriter = csv.writer(fu)
        csvwriter.writerows(dataCalls)
def chooseElevator():
    for k in calls:
        k.elevator = random.randint(0, len(building._elevators))

if __name__ == "__main__":
    building = Building("input\Ex1_input\Ex1_Buildings\B2.json")
    calls = readCalls("input\Ex1_input\Ex1_Calls\Calls_a.csv")
    chooseElevator()
    writeCalls()
    print(building._elevators[1].__dict__)
    print(calls[0].__dict__)
    