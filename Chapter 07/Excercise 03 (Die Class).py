"""
Chapter 09, Excercise 03
Purpose: Representing a die by a class type
"""
from random import randint


class Die(object):
    """Represents a die"""
    def __init__ (self, initNum = 1):
        """Creates a diw with the given value or a default value of 1"""
        self.num = initNum

    def getvalue(self):
        """Returns the die's value"""
        return self.num

    def roll(self):
        """Resets the die's value to a random number between 1 and 6"""
        self.num = randint(1,6)

    def __str__(self): #operator overload print function
        """Returns a string representation of a die"""
        return "Value: " + str(self.num)

    def __gt__(self, other):
        """greater than operator overloading"""
        return self.num > other.num

    def __eq__(self,other):
        """The equality operator"""
        if self is other: #the same object
            return True
        elif type(self) != type(other): #type mismatch
            return False
        else:
            return self.num == other.num #have the same value or not

def main():
    """The main function of this program"""
    #represent two dice
    d1 = Die(2)
    d2 = Die()

    print(d1)
    print(d2)

    d1.roll()
    d2.roll()
    print(d1)
    print(d2)


    #comparing d1 and d2
    if d1 > d2:
        print("d1 is larger")
    else:
        print("d2 is greater than or equal")

    #compare d1 and d2
        if d1 == d2:
            print("d1 is equal to d2")
        else:
            print("d1 is not equal to d2")

main()
