import numpy as np

triangles = np.loadtxt('input.txt').T.flatten()
triangles = np.array(np.array_split(triangles, len(triangles) / 3))
print(np.sum(np.max(triangles, axis=1) < np.sum(triangles, axis=1) -
             np.max(triangles, axis=1)))

