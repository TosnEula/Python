"""
Chapter 06, Excercise 01
Purpose: compute the sum of positive integers from 1 to N recursively,
        Where N >= 1
"""

def main():
    """ The main function of the program """

    #prompt for the N
    num = int(input("Please enter a positive integer that is greater than or equal to 1: "))

    #Compute the sum from 1 to N
    sum = sumOneToN(num)

    #display the sum
    print("The sum from 1 to ", num, " is ", sum)

def sumOneToN(n):
    """Compute the sum from 1 to n recursively"""

    if n==1:
        return 1
    else:
        return sumOneToN(n-1) +n

main()
