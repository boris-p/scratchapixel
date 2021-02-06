# get the mean for tossing a die(1-6) X times

import pathlib
import matplotlib.pyplot as plt
import random

BASE_PATH = pathlib.Path(pathlib.Path(__file__).parent, 'artifacts')

NUM_OF_TOSSES = 2000
mean = 0
sum = 0
mean_prog = []  # mean progress as we toss more and more dies
tosses_range = range(NUM_OF_TOSSES)
for i in tosses_range:
    sum += random.randint(1, 6)
    mean = sum / (i+1)
    mean_prog.append(mean)


# Plot the points using matplotlib
plt.plot(tosses_range, mean_prog)
plt.xlabel('tosses')
plt.ylabel('mean')
plt.title('die tosses mean')
plt.savefig(f'{BASE_PATH}/die_tosses_mean.png')
