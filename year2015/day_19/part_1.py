import re

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

mol_set = set()
for left_repl, right_repl in replacements:
    for left_length in range(len(molecule)):
        if molecule[left_length:left_length+len(left_repl)] == left_repl:
            y = molecule[:left_length] + right_repl +\
                molecule[left_length + len(left_repl):]
            mol_set.add(y)
print(len(mol_set))
