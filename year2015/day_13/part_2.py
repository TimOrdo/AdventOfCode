import re
import itertools
from collections import deque


pattern_01 = re.compile(r'[A-Z]\w+')

names_set = set()
data = list()
with open("input.txt") as file:
    for line in file.read().splitlines():
        names = re.findall(pattern_01, line)
        names_set.add(names[0])
        help_list = list()
        help_list += names
        number = int(re.findall(r'\d+', line)[0])
        if 'gain' in line:
            help_list.append(number)
        elif 'lose' in line:
            number = -number
            help_list.append(number)
        data.append(help_list)

    variations = list(itertools.permutations(names_set))

max_happiness = 0
for item in variations:
    n_item = deque(item)
    local_happiness = 0
    for i in range(len(item) - 1):
        for name in data:
            if n_item[0] == name[0] and n_item[1] == name[1]:
                local_happiness += name[2]
            if n_item[0] == name[1] and n_item[1] == name[0]:
                local_happiness += name[2]
        n_item.rotate(1)
    if local_happiness > max_happiness:
        max_happiness = local_happiness

print(max_happiness)
