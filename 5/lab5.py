print("\n----------------------- t1: ------------------")
import numpy as np
scores = [78, 85, 92, 60, 88]
scores = np.array([4, 8, 15, 16, 23])
print(scores)
print(scores.shape)
print(scores.dtype)
print("\n----------------------- t2: ------------------")
quiz_grid = np.array([
 [90, 85, 78, 92],
 [70, 88, 95, 60],
 [82, 77, 91, 84],
])
print(quiz_grid)
print(quiz_grid.shape)
print(quiz_grid.ndim)
print(quiz_grid[0])
print(quiz_grid[0][2])

print("\n----------------------- t3: ------------------")
print(quiz_grid[0:2])
print(quiz_grid[:, 0])
print( quiz_grid[-1, -1])

print("\n----------------------- t4: ------------------")
quiz_grid[:, 2] = quiz_grid[:, 2] + 5
print(quiz_grid)
print(quiz_grid.mean(axis=1))
print(quiz_grid.max(axis=1))

print("\n----------------------- t5: ------------------")
averages = quiz_grid.mean(axis=1)
passed= averages >= 80
print(passed)
print(averages[passed==True])
print(f"Number who passed: {np.count_nonzero(passed)}")
