result = 0

with open("input.txt") as file:
    for line in file.read().splitlines():
        input_line = list(map(int, line.split('\t')))
        input_line.sort(reverse=True)

        for index, item in enumerate(input_line[:-1]):
            for tiny_item in input_line[index + 1:]:
                if item % tiny_item == 0:
                    result += item // tiny_item

print(result)
