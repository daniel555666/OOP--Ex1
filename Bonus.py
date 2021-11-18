import csv
import time
from tkinter import *


def readElevators() -> list:
    elev = []
    with open("elevatorPos.csv") as fp:
        data = csv.reader(fp)
        for line in data:
            elev.append(line)
    return elev


def drawLines():
    i = high
    while i <= size:
        w.create_line(0, i, size, i, fill="black", width=3)
        i += high

    i = width
    while i <= size:
        w.create_line(i, 0, i, size, fill="black", width=3)
        i += width


if __name__ == "__main__":
    elevatorsPos = readElevators()
    minFloor = int(elevatorsPos[0][0])
    maxFloor = int(elevatorsPos[0][1])
    elevatorsPos.pop(0)
    sizeOfBuilding = maxFloor - minFloor
    size = 1000
    high = size/sizeOfBuilding
    width = size/len(elevatorsPos[0])
    master = Tk()
    w = Canvas(master, width=size, height=size)
    w.pack()
    
    for line in elevatorsPos:
        w.delete("all")
        for i in range(len(line)):
            drawLines()
            x1 = int(i*width)
            y1 = (-1*int(line[i]) + (maxFloor-1))*high
            x2 = (i+1)*width
            y2 = y1 + high
            w.create_rectangle(x1, y1, x2, y2, fill="blue")
            
        
        master.update_idletasks()
        master.update()
        time.sleep(0.05)
        
    # master.mainloop()
    


"""
w.create_rectangle(50, 20, 150, 80, fill="#476042")
w.create_rectangle(65, 35, 135, 65, fill="yellow")
w.create_line(0, 0, 50, 20, fill="#476042", width=3)
w.create_line(0, 100, 50, 80, fill="#476042", width=3)
w.create_line(150,20, 200, 0, fill="#476042", width=3)
w.create_line(150, 80, 200, 100, fill="#476042", width=3)
"""
