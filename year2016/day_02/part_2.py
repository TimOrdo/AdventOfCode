import numpy as np


keypad = np.array([
    ['', '', '1', '', ''],
    ['', '2', '3', '4', ''],
    ['5', '6', '7', '8', '9'],
    ['', 'A', 'B', 'C', ''],
    ['', '', 'D', '', ''],
])

answer = list()
with open("input.txt") as file:
    x = 0
    y = 2
    for line in file.read().splitlines():
        for item in line:
            try:
                if item == 'U' and keypad[y-1, x] != '':
                    y -= 1
                elif item == 'D' and keypad[y+1, x] != '':
                    y += 1
                elif item == 'R' and keypad[y, x+1] != '':
                    x += 1
                elif item == 'L' and keypad[y, x-1] != '':
                    x -= 1
            except IndexError:
                continue
            if x > 4:
                x = 4
            elif x < 0:
                x = 0
            if y > 4:
                y = 4
            elif y < 0:
                y = 0
            current_button = keypad[y, x]
        answer.append(keypad[y, x])
print(''.join(map(str, answer)))
