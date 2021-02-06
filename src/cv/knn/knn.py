# an implementation of k nearest neighbour algorithm following the following tutorial
# another important thing to do that I haven't done here is to normalize the data
# good explenation here - https://stats.stackexchange.com/questions/287425/why-do-you-need-to-scale-data-in-knn

from math import sqrt
import pathlib


# the dataset structure:
# Sepal length in cm.
# Sepal width in cm.
# Petal length in cm.
# Petal width in cm.
# Class

BASE_PATH = pathlib.Path(pathlib.Path(__file__).parent, 'artifacts')
IRISES = f'{BASE_PATH}/irises.csv'
K = 3


def prepare_dataset():
    data = []
    with open(IRISES) as f:
        for line in f:
            data.append(prepare_data_row(line))
    return data


def euclidean_distance(r1, r2):
    dist = 0
    # last column is the label
    for i in range(len(r1) - 1):
        dist += (float(r1[i]) - float(r2[i]))**2
    return sqrt(dist)


def get_neighbors(train_data, test_row, k):
    neighbors = []
    for train_row in train_data:
        dist = euclidean_distance(train_row, test_row)
        neighbors.append((train_row, dist))
    neighbors.sort(key=lambda tup: tup[1])

    return neighbors[:k]


def prepare_data_row(row_str):
    return [i.strip() for i in row_str.split(',')]


def main():
    dataset = prepare_dataset()

    test_row = prepare_data_row("6.3, 2.3, 4.4, 1.3, Iris-versicolor")
    # test_row = prepare_data_row("6.8, 3.2, 5.9, 2.3, Iris-virginica")

    neighbors = get_neighbors(dataset, test_row, K)

    print(neighbors)


main()
