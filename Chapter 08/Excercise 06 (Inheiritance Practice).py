"""
Chapter 09, Excercise 06
purpose: Have the Point3D class inherited (extends) the Point2D class
"""

#the super class(parent class)
class Point2D(object):
    """Represents a 2D point"""

    def __init__ (self, initX, initY):
        """contstructor"""
        self.x = initX
        self.y = initY

    def move(self, newX, newY):
        """moves the 2D point to a new location"""
        self.x = newX
        self.y = newY

    def home (self):
        """moves the 2D point to the origin"""
        self.x = 0
        self.y = 0

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

def main():
    """The main of the function"""

    #Create two 2D points
    location1 = Point2D(5,10)
    location2 = Point2D(57,7)

    print(location1)

    
main()
