import msvcrt as mvt


o = 0
with open("input.txt", "r") as file:
    for index, i in enumerate(file.read(), start=1):
        if i == "(":
            o += 1
        elif i == ")":
            o -= 1
print(o)
