class CallForElevator:
    def __init__(self, data):
        self.name = data[0]
        self.time = data[1]
        self.src = data[2]
        self.dest = data[3]
        self.state = data[4]
        self.elevator = data[5]