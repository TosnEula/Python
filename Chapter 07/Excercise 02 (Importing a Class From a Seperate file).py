"""
Chapter 07, Excercise 02
Purpose: Represent a student by a class type that is defined in a module
"""

from Student import *


#instantiate a student
myStudent = Student("Albert", 98)
print(myStudent)

myStudent.setName("Bob")
print("\n", myStudent)
