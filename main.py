import turtle
from scipy import signal
import random
import numpy as np
import math
crush = turtle.Turtle()

line_length = 30

colors = ['red', 'yellow', 'blue', 'green']
rand_data = np.random.normal(loc=0.0, scale=4, size=50)

horse_info = {}
round_num = 0

money = 1e6


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

    radius = 2 * rand_data[depth % len(rand_data)]

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
    gen_tree((0, 0), 4)
    """ normal_dist = np.random.normal(loc=0, scale=5, size=500)

    for value in normal_dist:
        crush.forward(2)
        crush.left(value)
        crush.forward(2)
        crush.left(value)
         crush.color("black", colors[i % 4])
        crush.begin_fill()
        crush.circle(5, 360)
        crush.end_fill()
 """
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

    # keep track of the round
    round_num += 1

    # add or update each horse in the global dictionary
    for horse in state.horses:
        if horse in horse_info:
            # if horse already exists, average its last round's outcome with its existing runtime
            existing_outcome = horse_info[horse][0]
            next_outcome = (existing_outcome + state['outcomes'][horse]) / 2
            horse_info[horse][0] = next_outcome
        # if horse doesn't exist, add it to dictionary
        horse_info[horse] = (10, state['features'][horse])

    # only bet after 100 rounds have happened, (gives good idea of how horses would perform)
    if round_num > 100:
        # get all the averaged outcomes
        pred_outcomes = [horse_info[horse][0] for horse in state['horses']]

        # get minimum runtime and the associated horse (fastest horse)
        min_outcome = 10
        min_index = 0
        for horse_index, outcome in enumerate(pred_outcomes):
            if outcome < min_outcome:
                min_outcome = outcome
                min_index = horse_index
    else:
        # bet nothing if not past 100 rounds
        return ("", 0)

    min_runtime = 10
    min_horse = ""
    for horse, outcome in state['outcomes'].items():
        if outcome < min_runtime:
            min_runtime = outcome
            min_horse = horse

    # get minimum runtime and the associated horse (fastest horse)
    min_outcome = 10
    min_index = 0
    for horse_index, outcome in enumerate(pred_outcomes):
        if outcome < min_outcome:
            min_outcome = outcome
            min_index = horse_index

    return (state['horses'][min_index], 10)


if __name__ == "__main__":
    filepath = "image.jpg"
    do_art(filepath)
