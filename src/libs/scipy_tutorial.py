# scipy builds on numpy and provides a large number of functions that operate on numpy arrays
import os
import pathlib
import numpy as np
from imageio import imread, imsave
from skimage.transform import resize
from scipy.spatial.distance import pdist, cdist, squareform

import matplotlib.pyplot as plt


BASE_PATH = pathlib.Path(pathlib.Path(__file__).parent, 'assets')

# image operations
CAT_PATH = pathlib.Path(BASE_PATH, 'cat.jpg')
img = imread(CAT_PATH)

# We can tint the image by scaling each of the color channels
# by a different scalar constant. The image has shape (400, 248, 3);
# we multiply it by the array [1, 0.95, 0.9] of shape (3,);
# numpy broadcasting means that this leaves the red channel unchanged,
# and multiplies the green and blue channels by 0.95 and 0.9
# respectively.

img_tinted = img * [1, 0.95, 0.9]
img_tinted = resize(img_tinted, (300, 300))

# plot the image
plt.subplot(1, 2, 1)
plt.imshow(img)


# A slight gotcha with imshow is that it might give strange results
# if presented with data that is not uint8. To work around this, we
# explicitly cast the image to uint8 before displaying it.
plt.subplot(1, 2, 2)
plt.imshow(np.uint8(img_tinted))
plt.savefig(f'{BASE_PATH}/cat_plot.png')

# could also save the image just as an image
imsave(f'{BASE_PATH}/new_cat.jpg', img_tinted)

# distance between points
# array of points
x = np.array([[0, 1], [1, 0], [2, 0]])
# Compute the Euclidean distance between all rows of x.
# d[i, j] is the Euclidean distance between x[i, :] and x[j, :],
# and d is the following array:
# [[ 0.          1.41421356  2.23606798]
#  [ 1.41421356  0.          1.        ]
#  [ 2.23606798  1.          0.        ]]
print(squareform(pdist(x, 'euclidean')))

print('-------------')
a = np.array([[0, 0, 0],
              [0, 0, 1],
              [0, 1, 0],
              [0, 1, 1],
              [1, 0, 0],
              [1, 0, 1],
              [1, 1, 0],
              [1, 1, 1]])
b = np.array([[0.1,  0.2,  0.4]])
print(cdist(a, b, 'euclidean'))
