"""
Chapter 07, Excerecise 01
Purpose: represent a student by a class type
"""

class Student(object):
    """Represents a student"""
    def __init__(self, initName, initScore):
        """The constructor that create a student based on the given initial values"""
        self.name = initName
        self.score = initScore

    def getName(self):
        """Returns the student's name"""
        return self.name

    def setName(self, newName):
        """Resets the student's name"""
        self.name = newName

    def getScore(self):
        """Returns the student's score"""
        return self.score

    def setScore(self, newScore):
        """ Sets the student's score"""
        self.score = newScore

    def __str__ (self):
        """Returns a string representation of the student"""
        return "Name: " + self.name +  "\nScore: " + str(self.score)

#instantiate a student
myStudent = Student("Albert", 98)
print(myStudent)

myStudent.setScore(60)
print(myStudent.getScore())

myStudent.setName("Bob")
print("\n", myStudent)
