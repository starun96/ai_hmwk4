import turtle
from scipy import signal
import random
import numpy as np
import math
crush = turtle.Turtle()

line_length = 30

colors = ['red', 'yellow', 'blue', 'green']


def draw_line(center, heading, line_length, radius):
    crush.penup()
    crush.setpos(center)
    crush.setheading(heading)
    crush.forward(radius)
    crush.pendown()
    crush.forward(line_length)
    crush.left(line_length)
    crush.penup()
    crush.forward(radius)

    return (crush.pos(), crush.heading())


def gen_tree(center, depth, heading=90, angle_span=120):
    """ 
    @param point where the circle will be drawn
    @param depth how many times to recurse 
    @param heading the general direction in which the turtle will form the 3 lines
    @param angle_span how wide out the lines will span (in terms of angle)

    recursively draw a circle and then 3 lines sticking out of it (which are the new centers for successive circles) until depth 0 
    the angle span and heading angle specify the sector of the circle from which the lines will be jutting out (if the angle span is 120 and the heading is 0, then lines with headings 0, -60 (300), and 60 will be drawn from the center of the circle). 

    first draw the circle around the [center], then go back to the center and set heading to [heading]. go forward by radius of circle (pen not on canvas). then go forward by the line length (pen on canvas). Record location as new center and the heading as the new heading. Go back to [center] and set heading to [heading - angle_span / 2]. repeat drawing the line. Go back to [center] and set heading to [heading + angle_span /2]. repeat drawing the line. 

    Recursively call gen_tree on the 3 new points with 1/3 the original angle_span, the new center and heading, and depth - 1.
     """
    new_center_headings = []

    radius = 10

    # draw circle at [center]
    crush.penup()
    crush.color("black", colors[depth % 4])

    crush.setpos(center)
    crush.forward(radius)
    crush.left(90)
    crush.pendown()
    crush.begin_fill()
    crush.circle(radius, 360)
    crush.end_fill()

    if depth > 0:
        # draw first line
        new_center_heading = draw_line(center, heading, line_length, radius)
        new_center_headings.append(new_center_heading)

        # draw second line
        new_center_heading = draw_line(
            center, heading - angle_span / 2, line_length, radius)
        new_center_headings.append(new_center_heading)

        # draw third line
        new_center_heading = draw_line(
            center, heading + angle_span / 2, line_length, radius)
        new_center_headings.append(new_center_heading)

        # make recursive call if depth > 0
        for center_heading in new_center_headings:
            gen_tree(center_heading[0], depth - 1,
                     heading=center_heading[1], angle_span=angle_span / 3)


def do_art(filepath):
    """ generates and saves an image at the filepath s, returns    nothing """
    # initialize the turtle
    window = turtle.Screen()
    window.setup(width=800, height=600)
    crush.shape("turtle")
    crush.speed(0)

    # generate the circle tree
    #gen_tree((0, 0), 4)

    for i in range(4000):
        for j in range(20):
            crush.forward(math.sin(i / 10) * math.cos(j / 10) * 50)
            crush.left(10)
            """ crush.color("black", colors[i % 4])
            crush.begin_fill()
            crush.circle(5, 360)
            crush.end_fill() """

    turtle.done()


def bet(state):
    """ state is a dictionary that gives info about the current bet and the previous round's results
    returns ordered pair (horse-name, bet-amount) 

    state = {
        'horses': ['horse_name1', 'horse_name2', 'horse_name3', ...],


        # feature list for each horse (e.g. horse_name1's feature 0 is 0 and 2 for horse_name2)
        'features': {       
            'horse_name1': [0, 1, 2, 3.3, ...],
            'horse_name2': [2, 1, 1, 4.2, ...], ...

        },


        # time each horse last ran. if hasn't run yet, value is -1
        'outcomes': {
            'horse_name1': 3.5,
            'horse_name2': -1, 
            'horse_name3': 2.3, 
            ...
        },

        # the last bet for each team. if first round of a play, bets will be set to ("", -1)
        bets = {
            'team_name1': ("horse_name1", 4),
            'team_name2': ("horse_name2", 2), 
            ...
        }

    }
    """

    pass


if __name__ == "__main__":
    filepath = "image.jpg"
    do_art(filepath)
