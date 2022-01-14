"""
Assignment 06
Student Name: Dominique Shim
Purpose: This program creates a class that represents a tricycle.
"""


class Tricycle(object):
    """Represents a tricycle"""

    #Constructor
    def __init__ (self, initSpeed=0):        
        self.speed = initSpeed

    #getter method for speed
    def getSpeed(self):
        return self.speed

    #setter method for speed
    def setSpeed(self, initSpeed):
        self.speed = initSpeed

    #increase speed by 1
    def pedal(self):
        self.speed += 1

    #greater than overload function
    def __gt__ (self, other):
        return self.speed > other.speed

    #print overload function
    def __str__(self):
        return "speed: "+ str(self.speed)

def main():
    """The main function of this program"""

    #create two tricycles
    myTricycle = Tricycle(2)
    yourTricycle = Tricycle()

    #print both tricycles
    print("My tricycle has", myTricycle)
    print("Your tricycle has", yourTricycle)

    #change your tricycle's speed to 2
    yourTricycle.setSpeed(2)
 
    #pedal your tricycle
    yourTricycle.pedal()

    #print both tricycles again
    print("My tricycle has", myTricycle)
    print("Your tricycle has", yourTricycle)

    #check if my tricycle is running faster than your tricycle
    if (myTricycle > yourTricycle):
        print("My tricycle is running faster than your tricycle")
    else:
        print("My tricycle is not running faster than your tricycle")

main()
