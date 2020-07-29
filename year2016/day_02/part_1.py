keypad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

answer = list()


with open("input.txt") as file:
    x = 1
    y = 1
    for line in file.read().splitlines():
        for item in line:
            if item == 'U':
                y -= 1
            elif item == 'D':
                y += 1
            elif item == 'R':
                x += 1
            elif item == 'L':
                x -= 1
            if x > 2:
                x = 2
            elif x < 0:
                x = 0
            if y > 2:
                y = 2
            elif y < 0:
                y = 0
        answer.append(keypad[y][x])
print(''.join(map(str, answer)))
