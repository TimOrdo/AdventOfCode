import re


pattern = re.compile(r'\d+')

seconds = 2503
input_list = list()
with open("input.txt") as file:
    for line in file.read().splitlines():
        input_list.append(list(map(int, re.findall(pattern, line))))

answer_list = list()
for item in input_list:
    times = seconds // (item[1] + item[2])
    remain = seconds - times * (item[1] + item[2])
    if remain <= item[1]:
        answer_list.append(times * item[0] * item[1] + item[0] * remain)
    else:
        answer_list.append(times * item[0] * item[1] + item[0] * item[1])

print(max(answer_list))
