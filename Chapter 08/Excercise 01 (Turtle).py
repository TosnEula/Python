"""
Chapter 07, Excercise 01
Purpose: draw a square at a specified location with a specified length for each
"""

from turtle import *


def drawSquare(t, x, y, length):
    """draw a square at the starting location with the specified length for each"""

    #raise the pen
    t.up()
    #go to the location
    t.goto(x,y)
    #ready to draw, lower the pen
    t.down()
    #draw the square
    for count in range(4):
        t.forward(length)
        t.right(90)

def main():
    """main function"""
    #create a turtle
    goofy = Turtle()
    #hide the turtle body
    goofy.hideturtle()
    #change the pen color to red
    goofy.pencolor("red")
    #draw the square
    drawSquare(goofy, 100, 100, 60)


main()
