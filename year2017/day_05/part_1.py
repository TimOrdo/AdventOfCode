input_list = []
steps = 0
cur_index = 0

with open("input.txt") as file:
    for line in file.read().splitlines():
        input_list.append(int(line))

while True:
    try:
        timed_value = input_list[cur_index]
        input_list[cur_index] += 1
        cur_index += timed_value
        steps += 1
    except:
        print(steps)
        break
