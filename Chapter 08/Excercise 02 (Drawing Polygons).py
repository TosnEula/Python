"""
Chapter 07, Excercise 02
Purpose: drawing a polygon by connecting a list of verticies
"""

from turtle import *

def main():
    """The main function of the program"""
    #Intialize turtle
    greg = Turtle()

    #hide the turtle body
    greg.hideturtle()

    #draw the polygon
    drawPolygon(greg, [(-30,-20), (-20, 50), (30,60), (-63,70) ])

def drawPolygon(t, nodes):
    """Connecting a list of nodes to form a polygon"""

    #before drawing, raise the pen
    t.up()

    #go to the last node
    t.goto(nodes[-1])

    #ready to draw, lower the pen
    t.down()
    for (x,y) in nodes:
        t.goto(x,y)

main()
