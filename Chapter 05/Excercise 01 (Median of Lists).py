"""
Chapter 05, Excercise 01
Purpose: Find the median for a set of floating-point numbers in an input file
"""

from os.path import *

#Prompt for the input file name
fileName = input("Please enter a file name: ")

#Checks if the file exists
if exists(fileName):
    #Open the input file in reading mode
    inFile = open(fileName, "r")

    #build a list of numbers by using the numbers in the umput file
    numbers = []

    for line in inFile:
        words = line.split()
        for word in words:
            numbers.append(float(word))
        
    #sort the numbers in ascending order
    numbers.sort()

    #computer the median
    midpoint= len(numbers) // 2

    if len(numbers) % 2 == 1:
        median = (numbers[midpoint])
    else:
        median = (numbers[midpoint - 1] + numbers[midpoint]) / 2

    #print the median
    print("the median is: ", median)
else:
    print(fileName, "does not exist.")
