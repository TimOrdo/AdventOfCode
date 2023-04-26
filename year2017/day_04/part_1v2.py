counter = 0

with open("input.txt") as file:
    for line in file.read().splitlines():
        input_line = line.split(' ')
        if len(set(input_line)) == len(input_line):
            counter += 1

print(counter)
