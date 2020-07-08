import re


pattern = re.compile(r'\w+|.\d+')

a = 1
b = 0

instructions = list()
with open("input.txt") as file:
    for line in file.read().splitlines():
        instructions.append(line)


index = 0
while len(instructions) > index >= 0:
    result = re.findall(pattern, instructions[index])
    if 'hlf' in result:
        if 'a' in result:
            a /= 2
        elif 'b' in result:
            b /= 2
    elif 'tpl' in result:
        if 'a' in result:
            a *= 3
        elif 'b' in result:
            b *= 3
    elif 'inc' in result:
        if 'a' in result:
            a += 1
        elif 'b' in result:
            b += 1
    elif 'jmp' in result:
        index += int(result[1])
        continue
    elif 'jie' in result:
        if 'a' in result:
            if a % 2 == 0:
                index += int(result[2])
                continue
        elif 'b' in result:
            if b % 2 == 0:
                index += int(result[2])
                continue
    elif 'jio' in result:
        if 'a' in result:
            if a == 1:
                index += int(result[2])
                continue
        elif 'b' in result:
            if b == 1:
                index += int(result[2])
                continue
    index += 1

print(b)
