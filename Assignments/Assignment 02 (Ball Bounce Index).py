"""
Fall 2021 , COP 2034.01, Introduction to Programming Using Python
Assignment 02, Excercise 01
Student Name: Dominique Shim
Purpose: Finds the total distance a ball would travel depending on its bouncing index.
"""

#Define Variables
height = float(input("Please input the height: "))
index = float(input("Please input the bounce index: "))
bounce = int(input("Please input the amount of bounces: "))
total = 0
count = 0

#Should the bounce index be greater than 1 or less than 0 the program will stop
if index >= 1 or index <= 0:
    print ("The index has to be between 1 and 0.")
    exit()
    

#Calculate the total distance travelled and stops once the height is lower than 0.5 to stop infinetly loops.
while count < bounce:
    total += height + (height * index)
    height *= index
    count += 1

#Print the resulting distance
print ("The distance the ball travelled is: ",round (total,2))
