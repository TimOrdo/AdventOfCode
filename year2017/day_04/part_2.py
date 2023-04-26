counter = 0

with open("input.txt") as file:
    for line in file.read().splitlines():
        input_line = line.split(' ')
        sorted_input_line = [''.join(sorted(u)) for u in input_line]

        if len(set(sorted_input_line)) == len(input_line):
            counter += 1

print(counter)
