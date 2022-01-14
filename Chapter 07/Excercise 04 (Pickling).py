"""
Chapter 09, Excercise 04
Purpose: Write an object to a file and then read it in from the file.
"""

from pickle import *

class Counter(object):
    """Represents a counter"""

    def __init__ (self, initValue=0):
        """"Default constructor"""
        self.value = initValue

    def getValue(self):
        """Returns the counter's value"""
        return self.value

    def setValue(self, newValue):
        """Resets the counter;s value"""
        self.value = newValue

    def __str__ (self):
        """Returns a string representation of the counter"""
        return "Value:  " + str(self.value)

class main():
    """The main function of this program"""
    #create a counter with initial value 3
    aCounter = Counter(3)

    #print the counter
    print(aCounter)

    #prompt for a file name
    fileName = input("Please enter a file name: ")

    #Open the output file
    outFile = open(fileName,"wb")

    #write the counter to the outpur file
    dump(aCounter, outFile)

    #close the output file
    outFile.close()

    #Open the input file
    inFile= open(fileName, "rb")

    #read in the counter from the input file
    aCounter = load(inFile)

    #print the counter again
    print(aCounter)

main()
