import numpy as np


input_list = list()
with open("input.txt") as file:
    for line in file.read().splitlines():
        input_list.append(list(line))

input_list = np.array(input_list)
help_list = input_list.copy()

number = 100
for _ in range(number):
    for str_i in range(len(help_list)):
        for col_i in range(len(input_list)):
            if str_i == 0 and col_i == 0 \
                    or str_i == len(input_list) - 1 and col_i == len(input_list) - 1 \
                    or str_i == 0 and col_i == len(input_list) - 1 \
                    or str_i == len(input_list) - 1 and col_i == 0:
                continue
            l_str = str_i - 1
            r_str = str_i + 2
            u_col = col_i - 1
            l_col = col_i + 2
            if l_str < 0:
                l_str = 0
            if r_str > len(input_list):
                r_str = len(input_list)
            if u_col < 0:
                u_col = 0
            if l_col > len(input_list):
                l_col = len(input_list)
            helper = input_list[l_str:r_str, u_col:l_col]
            counter = 0
            for i in helper:
                for j in i:
                    if j == '#':
                        counter += 1
            if input_list[str_i, col_i] == '#':
                counter -= 1
            if input_list[str_i, col_i] == '#' and (counter == 2 or counter == 3):
                help_list[str_i, col_i] = '#'
            else:
                help_list[str_i, col_i] = '.'
            if input_list[str_i, col_i] == '.' and counter == 3:
                help_list[str_i, col_i] = '#'
    input_list = help_list.copy()

count = 0
for string in input_list:
    for column in string:
        if column == '#':
            count += 1
print(count)