import re


pattern = re.compile(r'\d+')

seconds = 2503
input_list = list()
with open("input.txt") as file:
    for line in file.read().splitlines():
        input_list.append(list(map(int, re.findall(pattern, line))))

range_list = [0] * len(input_list)
answer_list = [0] * len(input_list)
for time in range(seconds):
    for number, reindeer in enumerate(input_list):
        tru_time = time - time // (reindeer[1] + reindeer[2]) * (reindeer[1] + reindeer[2])
        if tru_time < reindeer[1]:
            range_list[number] += reindeer[0]
    for index, item in enumerate(range_list):
        if item == max(range_list):
            answer_list[index] += 1

print(max(answer_list))
