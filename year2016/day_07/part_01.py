import re

answer = 0

with open("input.txt") as file:
    for line in file.read().splitlines():
        checker = False
        parts = re.split(r'\[|\]', line)

        for index in range(len(parts)):
            if index % 2 != 0:
                if re.findall(r'(.)(.)\2\1', parts[index]):
                    checker = False
                    break
            else:
                if re.findall(r'(.)(.)\2\1', parts[index]) and not re.findall(r'(.)\1{3,}', parts[index]):
                    checker = True
        if checker is True:
            answer += 1

print(answer)
