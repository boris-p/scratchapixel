import math
import pathlib
import matplotlib.pyplot as plt


BASE_PATH = pathlib.Path(pathlib.Path(__file__).parent, 'artifacts')
fc = math.factorial

# calculating the chance that when tossing a coin six times two time will be heads (let's say heads means 1)

NUM_OF_SAMPLES = 10


def calc_tosses_prob(n):
    # n = number of samples to be 1
    p = 0.5  # the probability of one toss
    N = NUM_OF_SAMPLES  # number of samples
    # counts the number of ways in which n of the N samples takes 1
    c = fc(N) / (fc(n) * fc(N - n))
    return c * math.pow(p, n) * math.pow(1-p,  N-n)


tosses = range(NUM_OF_SAMPLES+1)
outcomes = [calc_tosses_prob(i) for i in tosses]


x = tosses
y = outcomes

# Plot the points using matplotlib
plt.scatter(x, y)
plt.plot(x, y)
for i, val in enumerate(y):
    plt.annotate(round(val, 2), (x[i], y[i]))
plt.xlabel('tosses')
plt.ylabel('probability')
plt.title('Coin tosses distribution')
plt.savefig(f'{BASE_PATH}/coin_toss_binomial_dist.png')
