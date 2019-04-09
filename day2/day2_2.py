def feet_of_ribbon(l: int, w:int, h: int) -> int:
    return 2*(l + w + h - max(l, w, h)) + l * w * h


ft_of_paper: int = 0
with open("input.txt") as file:
    for line in file.read().splitlines():
        ft_of_paper += feet_of_ribbon(
            int(line.split('x')[0].strip()),
            int(line.split('x')[1].strip()),
            int(line.split('x')[2].strip())
        )
print(ft_of_paper)
