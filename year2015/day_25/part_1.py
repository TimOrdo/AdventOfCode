from collections import namedtuple

Coordinates = namedtuple('Coordinates', ('x', 'y'))


def next_code(previous_code):
    return (previous_code * 252533) % 33554393


x = 1
y = 1
current_code = 20151125
coordinates = Coordinates(3029, 2947)

while True:
    if y == 1:
        y = x + 1
        x = 1
    else:
        x += 1
        y -= 1
    current_code = next_code(current_code)
    if x == coordinates.x and y == coordinates.y:
        print(current_code)
        break
