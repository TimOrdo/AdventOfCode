import re

answer = 0

with open("input.txt") as file:
    for line in file.read().splitlines():

        parts = re.split(r'\[|\]', line)
        in_square = list()
        out_square = list()

        for index in range(len(parts)):
            if index % 2 != 0:
                in_square += re.findall(r'(.)(.)\1', parts[index])
            else:
                out_square += re.findall(r'(.)(.)\1', parts[index])

        for item in in_square:
            helper = list(item)
            helper.reverse()
            if tuple(helper) in out_square:
                answer += 1
                break
print(answer)