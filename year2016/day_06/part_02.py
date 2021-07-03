import numpy as np
import string

input_list = []

with open("input.txt") as file:
    for line in file.read().splitlines():
        input_list.append([x for x in line])

transpose_matrix_input = np.transpose(np.array(input_list))
answer = ''

for item in transpose_matrix_input:
    count = len(string.ascii_lowercase)
    password_letter = ''
    for letter in string.ascii_lowercase:
        if count > np.count_nonzero(item == letter):
            count = np.count_nonzero(item == letter)
            password_letter = letter
    answer += password_letter

print(answer)
