with open("input.txt", "r") as file:
    my_input = list(map(int, file.read()))

sum_result = 0

for index, item in enumerate(my_input):
    if index + 1 == len(my_input) and item == my_input[0]:
        sum_result += item
        break
    if item == my_input[index + 1]:
        sum_result += item

print(sum_result)
