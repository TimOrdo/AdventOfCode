counter = 0

with open("input.txt") as file:
    for line in file.read().splitlines():
        checker = True
        input_line = line.split(' ')
        for item in input_line:
            if input_line.count(item) > 1:
                checker = False
                break
        if checker:
            counter += 1

print(counter)
