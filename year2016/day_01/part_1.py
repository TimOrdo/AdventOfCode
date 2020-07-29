import math
import re


def rotate(angle: float, start_point: list, end_point: list):
    new_x = (end_point[0] - start_point[0]) * math.cos(angle) - \
            (end_point[1] - start_point[1]) * math.sin(angle) + start_point[0]
    new_y = (end_point[0] - start_point[0]) * math.sin(angle) + \
            (end_point[1] - start_point[1]) * math.cos(angle) + start_point[1]
    return int(round(new_x, 1)), int(round(new_y, 1))


points = [[0, 0]]
pattern = re.compile(r'\d+')
current_angle = math.pi / 2

with open("input.txt", "r") as file:
    rotation_list = file.read().split(', ')

for r_index, rotation in enumerate(rotation_list):
    point = points[r_index].copy()
    point[0] += int(re.findall(pattern, rotation)[0])
    if 'R' in rotation:
        current_angle -= math.pi / 2
    elif 'L' in rotation:
        current_angle += math.pi / 2
    points.append(list(rotate(current_angle, points[r_index], point)))

print(sum(map(abs, points[-1])))
