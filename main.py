def do_art(s):
    """ generates and saves an image at the filepath s, returns nothing """
    pass


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
