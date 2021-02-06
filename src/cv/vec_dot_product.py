import numpy as np
w = [0.2, -0.5, 0.1, 2.0]
pixels_col = [56, 231, 24, 2]

ww = np.array(w)
pixels_col1 = np.array(pixels_col)


res = 0
for i, num in enumerate(w):
    res += num * pixels_col[i]
print(res)


print(np.sum(np.multiply(ww, pixels_col1)))
print(np.sum(ww * pixels_col1))
print(ww.dot(pixels_col1))
