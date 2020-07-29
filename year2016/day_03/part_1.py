import numpy as np

triangles = np.loadtxt('input.txt')
print(np.sum(np.max(triangles, axis=1) < np.sum(triangles, axis=1) -
             np.max(triangles, axis=1)))
