"""
Chapter 06, Excercise 05
Purpose: raise x to the power of N recursively, where x is a floating point number
         and N is an integer than or equal to 1
"""

def main():
    """The main function of this program"""

    #prompt user to give x
    base = float(input("Please enter the base which is a floating point number: "))

    #prompt for the exponent, N
    exponent = int(input("Please enter the exponent which is a integer greater than or equal to 1: "))

    result = pow(base,exponent)

    print(result)

def pow(x, n):
    """Raise n to the nth"""
    if n== 1:
        return x #base case
    else:
        return pow(x, n-1) * x #recurcisve case

main()
