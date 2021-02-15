# consider some phenomenon of interest and have a number of observations
# each observation has two of more features and we try to establish a relationship between them

# in other words we need to find a function that maps some
# features or variables to others sufficiently well

# it is common do denote outputs with a y and inputs
# (independent variables) with an x

# if there are two or more independent variables they can be represented as a vector
# x = (x1, x2, ...)


# simple (single variate) linear regression is where there's one x -  𝑓(𝑥) = 𝑏₀ + 𝑏₁𝑥

# multiple linear regression. If there are two independent variables - 𝑓(𝑥₁, 𝑥₂) = 𝑏₀ + 𝑏₁𝑥₁ + 𝑏₂𝑥₂
# represents a regressions plane in three dimentional plane

# coefficient of determination, denoted as 𝑅², tells you which amount
# of variation in 𝑦 can be explained by the dependence on 𝐱 using the
# particular regression model. Larger 𝑅² indicates a better fit and means
# that the model can better explain the variation of the output with
# different inputs

# The value 𝑅² = 1 corresponds to SSR = 0, that is to the perfect fit since
# the values of predicted and actual responses fit completely to each other

# https://realpython.com/linear-regression-in-python/

import numpy as np
import pathlib

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

BASE_PATH = pathlib.Path(pathlib.Path(__file__).parent, 'artifacts')


def plot_data(x, y):
    plt.scatter(x, y)
    for i, val in enumerate(y):
        plt.annotate(val, (x[i], y[i]))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('data')
    plt.savefig(f'{BASE_PATH}/base_data.png')


def plot_data_with_line(x, y, slope, intercept):
    x1 = np.arange(np.min(x), np.max(x), 1)
    y1 = slope * x1 + intercept
    plt.plot(y1)
    plt.scatter(x, y)
    for i, val in enumerate(y):
        plt.annotate(val, (x[i], y[i]))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('data and estimation line')
    plt.savefig(f'{BASE_PATH}/base_data_with_lin_regression.png')


# provide data
_x = [5, 15, 25, 35, 45, 55]
_y = [5, 20, 14, 32, 22, 38]
x = np.array(_x).reshape((-1, 1))
y = np.array(_y)
print("x is", x)
print("y is", y)


plot_data(x, y)


#  calculate the optimal values of the weights 𝑏₀ and 𝑏₁,
# using the existing input and output (x and y) as the arguments
model = LinearRegression().fit(x, y)

# we can obtain the coefficient of determination (𝑅²)
r_sq = model.score(x, y)
print("coefficient of determination:", r_sq)

print('intercept (𝑏₀):', model.intercept_)
print('slope (𝑏₁):', model.coef_)
plot_data_with_line(x, y, slope=model.coef_,  intercept=model.intercept_)


# we can alo provide y as a 2-d array
# in which case intercept will be a one dimentional array and coef
# will be a two dimensional array

new_model = LinearRegression().fit(x, y.reshape((-1, 1)))
print('intercept (𝑏₀):', new_model.intercept_)
print('slope (𝑏₁):', new_model.coef_)

# once we have a model we're happy with we can start predicting
y_pred = model.predict(x)
print('predicted response:', y_pred, sep='\n')

# or by doing this
y_pred = model.intercept_ + model.coef_ * x
print('predicted response:', y_pred, sep='\n')

# we can flatten the result by replacing x with x.reshape(-1),
# x.flatten(), or x.ravel() when multiplying it with model.coef_.
y_pred = model.intercept_ + model.coef_ * x.flatten()
print('predicted response:', y_pred, sep='\n')

# we can also predict on new data
x_new = np.arange(5).reshape((-1, 1))
y_new = model.predict(x_new)
print(y_new)

# -------------------------------------------------------------------------
# ---------------------- multiple linear regression -----------------------
# -------------------------------------------------------------------------

# x is a two-dimensional array with at least two columns
x = [[0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35]]

# y is usually a one-dimensional array
y = [4, 5, 20, 14, 32, 22, 38, 43]

x, y = np.array(x), np.array(y)
model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)
print('coefficient of determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)

y_pred = model.predict(x)
print('predicted response:', y_pred, sep='\n')

# for more detailed results, it's also possible to use a library called statsmodels
