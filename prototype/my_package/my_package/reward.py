from math import log

def reward_function(unit_plays, total_plays):
    return 1 / (10 * ln(total_plays) + 1) * unit_plays**0.8

