"""
Chapter 06, Excercise 06
Purpose: Compute the Nth element in the Fibonacci sequence
"""

def main():
    """The main function of this program"""

    #prompt for the N
    num = int(input("Please enter a positive integer that is greater than or equal to 1: "))

    #Compute the Nth element in the Fibonacci sequence
    nthElement = fib(num)

    #Display the result
    print("The element is ", nthElement)

def fib(n):
    """Compute the nth element in the Fibonacci sequence"""

    if n <= 2:
        return n-1
    else:
        return fib(n-2) + fib(n-1)
    
main ()
