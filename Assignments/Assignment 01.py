"""
Fall 2021 , COP 2034.01, Introduction to Programming Using Python
Assignment 01, Excercise 01
Student Name: Dominique Shim
Purpose: Finding the weekly pay of a person by taking their hourly input.
"""




hrWage = float(input("Please put in your hourly wage: "))#Takes hours wage.
totHrs = float(input("Please put in your total regular hours: ")) #Takes normal amount of hours worked. 
overHrs = float(input("Please put in your total overtime hours: "))#Takes the amount of overtime hours for the week.

#calculates the total amount of money earned for the week.
overPay = (hrWage * overHrs) * 1.5
totPay = overPay + (totHrs * hrWage)

print("your weekly pay is:",totPay) #Displays weekly wage.
