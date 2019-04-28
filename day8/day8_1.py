with open("input.txt") as file:
    print(sum(len(line) - len(eval(line)) for line in file.read().splitlines()))
