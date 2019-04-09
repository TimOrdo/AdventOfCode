import re


template_one = re.compile(r'\d+')
light_map = [[0 for x in range(1000)] for x in range(1000)]
counter = 0
with open("input.txt") as file:
    for line in file.read().splitlines():
        coord_list = template_one.findall(line)
        if 'turn on' in line:
            for coord_x in range(int(coord_list[0]), int(coord_list[2]) + 1):
                for coord_y in range(int(coord_list[1]), int(coord_list[3]) + 1):
                    light_map[coord_x][coord_y] += 1
        elif 'turn off' in line:
            for coord_x in range(int(coord_list[0]), int(coord_list[2]) + 1):
                for coord_y in range(int(coord_list[1]), int(coord_list[3]) + 1):
                    light_map[coord_x][coord_y] -= 1
                    if light_map[coord_x][coord_y] < 0:
                        light_map[coord_x][coord_y] = 0
        elif 'toggle' in line:
            for coord_x in range(int(coord_list[0]), int(coord_list[2]) + 1):
                for coord_y in range(int(coord_list[1]), int(coord_list[3]) + 1):
                    light_map[coord_x][coord_y] += 2
print(sum(sum(x) for x in light_map))
