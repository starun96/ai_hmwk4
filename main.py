import turtle
from scipy import signal
import random


def gen_tree(center, heading, angle_span):
    turtle.setpos(center)
    turtle.setheading(heading)


def do_art(filepath):
    """ generates and saves an image at the filepath s, returns    nothing """
    # initialize the turtle
    window = turtle.Screen()
    window.setup(width=800, height=600, startx=10, starty=0.5)
    crush = turtle.Turtle()
    crush.shape("turtle")

    """ current = 0
    seen = set()

    # step sizes increase by 1 each time
    for step_size in range(1, 100):
        backwards = current - step_size

        if backwards > 0 and backwards not in seen:
            crush.setheading(90)
            crush.circle(step_size / 2, 180)
            current = backwards

            seen.add(current)

        else:
            crush.setheading(270)
            crush.circle(step_size/2, 180)
            seen.add(current) """

    current_pos = crush.position()
    crush.circle(30, 120)

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
