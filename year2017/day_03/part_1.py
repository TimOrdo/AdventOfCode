import math


def get_n(num: int):
    sqrt_num = math.sqrt(num)
    if sqrt_num % 1 == 0:
        return sqrt_num
    if int(sqrt_num) % 2 == 1:
        return int(sqrt_num) + 2
    if int(sqrt_num) % 2 == 0:
        return int(sqrt_num) + 1
    return 0


puzzle_input = 347991

n = get_n(puzzle_input)

lower_right = n*n
lower_left = n*n - (n - 1)
upper_left = n*n - 2*(n - 1)
upper_right = n*n - 3*(n - 1)

answer = 0
if lower_right >= puzzle_input > lower_left:
    answer = math.fabs(lower_right - puzzle_input - n//2) + n//2
if lower_left > puzzle_input > upper_left:
    answer = math.fabs(lower_left - puzzle_input - n//2) + n//2
if upper_left > puzzle_input > upper_right:
    answer = math.fabs(upper_left - puzzle_input - n//2) + n//2
if upper_right > puzzle_input:
    answer = math.fabs(upper_right - puzzle_input - n//2) + n//2

print(answer)
