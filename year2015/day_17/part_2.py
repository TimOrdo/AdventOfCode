import itertools as it


input_list = list()
with open("input.txt") as file:
    for line in file.read().splitlines():
        input_list.append(int(line))

quantity = list()
for i in range(2, len(input_list) + 1):
    for item in it.combinations(input_list, i):
        if sum(item) == 150:
            quantity.append(len(item))

print(quantity.count(min(quantity)))
