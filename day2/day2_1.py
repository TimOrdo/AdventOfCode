def feet_of_paper(l: int, w: int, h: int) -> int:
    return 2*(l * w + w * h + h * l) + min(l * w, w * h, h * l)


ft_of_paper: int = 0
with open("input.txt") as file:
    for line in file.read().splitlines():
        ft_of_paper += feet_of_paper(
            int(line.split('x')[0].strip()),
            int(line.split('x')[1].strip()),
            int(line.split('x')[2].strip())
        )
print(ft_of_paper)
