from collections import deque

checker = list()

with open("input.txt", "r") as file:
    my_input = deque(map(int, file.read().split('\t')))
    checker.append('.'.join(map(str, my_input.copy())))

while True:
    maxim = max(my_input)
    index = my_input.index(maxim)
    my_input.rotate(len(my_input) - index)
    my_input[0] = 0
    for i in range(maxim):
        my_input.rotate(-1)
        my_input[0] += 1
    my_input.rotate(maxim - len(my_input) + index)
    if checker.count('.'.join(map(str, my_input.copy()))) >= 1:
        # part 1
        print(len(checker))
        # part 2
        print(len(checker) - checker.index('.'.join(map(str, my_input.copy()))))
        break
    checker.append('.'.join(map(str, my_input.copy())))
