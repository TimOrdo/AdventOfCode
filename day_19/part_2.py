import re
from random import shuffle


pattern = re.compile(r'(\w+) => (\w+)')
input_list = list()
with open("input.txt") as file:
    for line in file.read().splitlines():
        input_list.append(line)
replacements = list()
for item in input_list[:-2]:
    result = re.findall(pattern, item)
    replacements.append(result[0])
molecule = input_list[-1]

shuffles = 0
count = 0
mol = molecule
while len(mol) > 1:
    start = mol
    for left_repl, right_repl in replacements:
        while right_repl in mol:
            count += mol.count(right_repl)
            mol = mol.replace(right_repl, left_repl)

    if start == mol:
        shuffle(replacements)
        mol = molecule
        count = 0
        shuffles += 1

print(count)
