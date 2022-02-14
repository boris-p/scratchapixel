# you are climbing a staircase. its takes n steps to reach to top.
# Each time we can take 1 or two step.
# how many distinct ways can we climb to the top?

# this is actually Fibonacci!

from typing import Dict


cache = {}


def climb_stairs(steps: int) -> int:

    if cache.get(steps) is not None:
        return cache.get(steps)
    if steps == 0:
        return 0
    if steps == 1:
        return 1

    return climb_stairs(steps - 1) + climb_stairs(steps - 2)


assert(climb_stairs(2)) == 2
assert(climb_stairs(1)) == 1
assert(climb_stairs(4)) == 5
