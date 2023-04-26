from collections import defaultdict


def area_sum(x, y, input_map):
    result_sum = 0
    for xx in range(x-1, x+2):
        for yy in range(y-1, y+2):
            result_sum += input_map[xx, yy]
    result_sum -= input_map[x, y]
    return result_sum


def spiral_run(puzzle_input):
    sp_map = defaultdict(int)
    sp_map[0, 0] = 1
    k, it = 1, 0

    stopper = True
    while stopper:
        it += 1
        k += 2
        for index in range(-it + 1, it):
            sp_map[it, index] = area_sum(it, index, sp_map)
            if sp_map[it, index] > puzzle_input:
                return sp_map[it, index]
        for index in reversed(range(-it + 1, it + 1)):
            sp_map[index, it] = area_sum(index, it, sp_map)
            if sp_map[index, it] > puzzle_input:
                return sp_map[index, it]
        for index in reversed(range(-it + 1, it + 1)):
            sp_map[-it, index] = area_sum(-it, index, sp_map)
            if sp_map[-it, index] > puzzle_input:
                return sp_map[-it, index]
        for index in range(-it, it + 1):
            sp_map[index, -it] = area_sum(index, -it, sp_map)
            if sp_map[index, -it] > puzzle_input:
                return sp_map[index, -it]


print(spiral_run(347991))
