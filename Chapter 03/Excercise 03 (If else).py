"""
Chapter 03, Excercise 03
Student Name: Dominique Shim
Purpose: Converting a numeric score into a letter grade based on the following scale:
         Invalid: above 100
         A: from 90 to 100
         B: from 80 to 89
         C: from 70 to 79
         F: from 0 to 69
         Invalid: below 0
"""

#enter a numeric score
score = int(input("Enter a numeric score (0 - 100): "))

#convert into a letter grade
if score > 100:
    grade = "INVALID"
elif score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "F"    
else:
    grade = "INVALID"

#display the letter grade
print("Your grade is: ", grade)
