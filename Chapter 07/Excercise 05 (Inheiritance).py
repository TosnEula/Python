"""
Chapter 09, Excercise 05
Purpose: the Dog class extends the pet class
"""

class Pet(object):
    """Represents a pet"""
    def __init__ (self,initAge):
         """Creates a pet with the given initial age"""
         age = initAge

    def getAge (self):
        """Returns the pet's age"""
        return self.age

    def setAge(self, newAge):
        """Resets the pet's age"""
        self.age = newAge


    def __str__(self):
        """returns a string representation of the pet"""
        return "Age: " + str(self.age)
    
#sub class
class Dog(Pet):
    """Represents a dog"""

    def __init__ (self, initAge, initName):
        Pet.setAge(initAge)
        self.name = initName

    def getName(self):
        return self.name

    def setName(self, newName)
        name = newName

    def __str__ (self):
        return Pet.__str__(self) + "\nName: " + self.name
