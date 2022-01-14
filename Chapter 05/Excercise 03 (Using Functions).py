"""
Chapter 05, Excercise 03
Purpose: define a square function to compute the square of a given floating point number
"""

#Main of the program
def main():
    #prompt user for a number
    number = float(input("Please input a number: "))

    #Compute and display the square of this number
    print("The square of ", number, " is ", square(number))

def square(number):
    return number * number


#start of the program
main()
