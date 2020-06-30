import numpy as np


input_number = 36000000
count = input_number // 10
street = np.zeros(count)
for house in range(1, count):
    street[house:50 * house:house] += 11 * house

print(min(np.where(street >= input_number)[0]))
