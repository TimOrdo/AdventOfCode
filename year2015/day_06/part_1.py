import re


template_one = re.compile(r'\d+')
light_map = [[False for x in range(1000)] for x in range(1000)]
counter = 0
with open("input.txt") as file:
    for line in file.read().splitlines():
        coord_list = template_one.findall(line)
        if 'turn on' in line:
            for coord_x in range(int(coord_list[0]), int(coord_list[2]) + 1):
                for coord_y in range(int(coord_list[1]), int(coord_list[3]) + 1):
                    light_map[coord_x][coord_y] = True
        elif 'turn off' in line:
            for coord_x in range(int(coord_list[0]), int(coord_list[2]) + 1):
                for coord_y in range(int(coord_list[1]), int(coord_list[3]) + 1):
                    light_map[coord_x][coord_y] = False
        elif 'toggle' in line:
            for coord_x in range(int(coord_list[0]), int(coord_list[2]) + 1):
                for coord_y in range(int(coord_list[1]), int(coord_list[3]) + 1):
                    light_map[coord_x][coord_y] = not (light_map[coord_x][coord_y])
for x in light_map:
    for y in x:
        if y is True:
            counter += 1
print(counter)
