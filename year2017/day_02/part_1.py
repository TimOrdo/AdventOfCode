result = 0

with open("input.txt") as file:
    for line in file.read().splitlines():
        input_line = list(map(int, line.split('\t')))
        result += max(input_line) - min(input_line)

print(result)
