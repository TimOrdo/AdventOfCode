import re
import itertools

input_list = list()
cities = set()
answeres = list()

with open("input.txt") as file:
    for line in file.read().splitlines():
        cities.add(re.findall(r"[A-Z]\w+|[0-9]\w+", line)[0])
        cities.add(re.findall(r"[A-Z]\w+|[0-9]\w+", line)[1])
        input_list.append(re.findall(r"[A-Z]\w+|[0-9]+", line))
cities_map = ([x for x in itertools.permutations(cities)])

for item in cities_map:
    helper = 0
    for list_item in input_list:
        for i in range(0, len(item) - 1):
            if item[i] in list_item and item[i+1] in list_item:
                helper += int(list_item[2])
    answeres.append(helper)

print(max(answeres))
