import sys
import random

class parameter:
    def __init__(self, name, minValue, maxValue):
        self.name = name
        self.minValue = minValue
        self.maxValue = maxValue
    
    def get_value(self):
        return random.randint(self.minValue,self.maxValue)

    def send_value(self):
        sys.stdout.write(self.name + "," + str(self.get_value()) + "\n")


def sender_interface():
    global parameter
    
    parameters_lst = [
        parameter("temperature",0,150),
        parameter("charge",0,100),
        parameter("daysSinceCreation",0,2000)
    ]

    for i in range(50):
        for parameter in parameters_lst:
            parameter.send_value()

if __name__ == '__main__':
    sender_interface()
