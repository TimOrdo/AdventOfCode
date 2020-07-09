way_of_santa = list()
way_of_santa.append((0, 0))
with open("input.txt", "r") as file:
    for item in file.read():
        if item == '^':
            way_of_santa.append((
                way_of_santa[-1][0],
                way_of_santa[-1][1] + 1)
            )
        elif item == '>':
            way_of_santa.append((
                way_of_santa[-1][0] + 1,
                way_of_santa[-1][1])
            )
        elif item == '<':
            way_of_santa.append((
                way_of_santa[-1][0] - 1,
                way_of_santa[-1][1])
            )
        elif item == 'v':
            way_of_santa.append((
                way_of_santa[-1][0],
                way_of_santa[-1][1] - 1)
            )
print(len(set(way_of_santa)))
