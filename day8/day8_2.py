import re


with open("input.txt") as file:
    answer = 0
    for line in file.read().splitlines():
        answer += len(re.findall(r"[\"|\\]", line)) + 2
print(answer)
