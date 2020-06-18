import re
import numpy as np


pattern = re.compile(r'-?\d+')
ingredients = list()
with open("input.txt") as file:
    for line in file.read().splitlines():
        ingredients.append(list(map(int, re.findall(pattern, line))))

input_matrix = ingredients
ingredients = np.array(input_matrix)[:, :-1]
m_calories = np.array(input_matrix)[:, -1:]
max_number = 0

for i in range(100):
    for j in range(100 - i):
        for k in range(100 - i - j):
            n = 100 - i - j - k
            helper = np.dot(np.array([i, j, k, n]), ingredients)
            helper[helper < 0] = 0
            answer = np.prod(helper)
            calories = np.dot(np.array([i, j, k, n]), m_calories)
            if max_number < answer and int(calories) == 500:
                max_number = answer

print(max_number)
