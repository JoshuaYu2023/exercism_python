"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    if power_pellet_active == True and touching_ghost == True:
        eaten = True
    else:
        eaten = False
    return eaten

def score(touching_power_pellet, touching_dot):
    if touching_power_pellet == True or touching_dot == True:
        point = True
    else:
        point = False
    return point


def lose(power_pellet_active, touching_ghost):
    if power_pellet_active != True:
        lost = True
    else:
        lost = False
    return lost


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    if has_eaten_all_dots == True and not (power_pellet_active == False and touching_ghost == True):
        huzzah = True
    else:
        huzzah = False
    return huzzah