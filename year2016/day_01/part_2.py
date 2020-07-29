import math
import re


def rotate(angle: float, start_point: list, end_point: list):
    new_x = (end_point[0] - start_point[0]) * math.cos(angle) - \
            (end_point[1] - start_point[1]) * math.sin(angle) + start_point[0]
    new_y = (end_point[0] - start_point[0]) * math.sin(angle) + \
            (end_point[1] - start_point[1]) * math.cos(angle) + start_point[1]
    return int(round(new_x, 1)), int(round(new_y, 1))


stretches = [[0, 0]]
pattern = re.compile(r'\d+')
current_angle = math.pi / 2

with open("input.txt", "r") as file:
    rotation_list = file.read().split(', ')

for r_index, rotation in enumerate(rotation_list):
    point = stretches[r_index].copy()
    point[0] += int(re.findall(pattern, rotation)[0])
    if 'R' in rotation:
        current_angle -= math.pi / 2
    elif 'L' in rotation:
        current_angle += math.pi / 2
    stretches[r_index] += rotate(current_angle, stretches[r_index], point)
    stretches.append(list(rotate(current_angle, stretches[r_index], point)))
stretches = stretches[:-1]

checker = True
ind = 0
while checker:
    x1 = stretches[ind][0]
    y1 = stretches[ind][1]
    x2 = stretches[ind][2]
    y2 = stretches[ind][3]
    if x1 == x2:
        for i in range(0, ind, 2):
            if y1 > y2:
                y1, y2 = y2, y1
            if y1 < stretches[i][1] < y2 and stretches[i][0] < x1 < \
                    stretches[i][2]:
                print(x1 + stretches[i][1])
                checker = False
                break
    elif y1 == y2:
        for i in range(1, ind, 2):
            if x1 > x2:
                x1, x2 = x2, x1
            if x1 < stretches[i][0] < x2 and stretches[i][1] < y1 < \
                    stretches[i][3]:
                print(stretches[i][0] + y1)
                checker = False
                break
    ind += 1

