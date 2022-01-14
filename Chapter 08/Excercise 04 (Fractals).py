"""
Chapter 08, Excercise 04
Purpose: Draw a C curve fractal to a given level recursively
"""

from turtle import *

def line (t, x1, y1, x2, y2):
    """Draw a line segment from (x1, y1) to (x1, y2)"""

    #before drawing
    t.up()
    t.goto(x1, y1)

    #start drawing
    t.down()
    t.goto(x2, y2)

def cCurve (t, x1, y1, x2, y2, level):
    """Draw the cCurve fractal to the given level"""

    if level == 0:
        line (t, x1, y1, x2, y2) #base case
    else:
        xm = (x1 + x2 + y1 - y2) // 2
        ym = (y1 + y2 + x2 - x1) // 2
        cCurve(t, x1, y1, xm, ym, level - 1)
        cCurve(t, xm, ym, x2, y2, level - 1)

def main():
    """The main of this program"""

    #prompt for the level of the fractal
    level = int(input("Please enter a level: "))

    #create a turtle
    goofy = Turtle()

    #hide the turtle's body
    goofy.hideturtle()

    #draw the C curve fractal
    cCurve(goofy, 0, 100, 0, -100, level)

#the entry point of execution
main()
