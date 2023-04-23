with open("input.txt", "r") as file:
    my_input = list(map(int, file.read()))

sum_result = 0
input_length = len(my_input)

for index, item in enumerate(my_input):
    if index // (input_length // 2) == 0:
        new_index = index + input_length // 2
        if item == my_input[new_index]:
            sum_result += item
    else:
        new_index = index + input_length // 2 - input_length
        if item == my_input[new_index]:
            sum_result += item

print(sum_result)
