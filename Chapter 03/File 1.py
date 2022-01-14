"""
Fall 2021 , COP 2034.01, Introduction to Programming Using Python
Assignment x, Excercise x
Student Name: xxx xxx
Purpose: Computing the average velocity of a moving object
         and round the result to 2 decimal palces
"""

#get time1, location1, time2 and location2
time1 = float(input("Please put in the first time: "))
location1 = float(input("Please put in the first location"))

time2 = float(input("Please put in the second time: "))
location2 = float(input("Please put in the second location: "))
#compute the average velocity
velocity = (location2-location1)/(time2-time1)
#round the result to 2 decimal places
display = round(velocity,2)
#display the result

print(display)

