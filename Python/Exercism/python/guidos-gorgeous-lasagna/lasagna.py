"""Functions used in preparing Guido's gorgeous lasagna.
This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40

PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

   :param elapsed_bake_time: the time it has already baked
   :return: remaining bake time after subtracting the passed time from expected time.

   This function takes the actual minutes the lasagna has been baking as
   an argument and returns how many minutes the lasagna still needs to bake
   based on the `EXPECTED_BAKE_TIME`.
   """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.

    :param number_of_layers: the number of lasagna layers made
    :return: int amount of prep time (in minutes), based on 2 minutes per layer added

    This function takes an integer representing the number of layers the lasagna has,
    calculating preparation time using a time of 2 minutes per layer added.
    """
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time.

    :param number_of_layers: the number of layers in the lasagna
    :param elapsed_bake_time: elapsed cooking time
    :return:  total time elapsed (in minutes) of the preping and cooking

    This function takes two integers representing the lasagna layers and the time already spent baking
     and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
