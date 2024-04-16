'''
Ghost Gobble Arcade Game

https://exercism.org/tracks/python/exercises/ghost-gobble-arcade-game
'''

def eat_ghost(power_pellet_active: bool, touching_ghost: bool) -> bool:
    eats_a_ghost: bool = power_pellet_active and touching_ghost
    return eats_a_ghost

def score(touching_power_pellet: bool, touching_dot: bool) -> bool:
    scores: bool = touching_power_pellet or touching_dot
    return scores

def lose(power_pellet_active: bool, touching_ghost: bool):
    loses: bool = touching_ghost and not power_pellet_active
    return loses

def win(has_eaten_all_dots: bool, power_pellet_active: bool, touching_ghost: bool) -> bool:
    wins: bool = not touching_ghost or (has_eaten_all_dots and power_pellet_active)
    return wins

print(win(True, False, False))