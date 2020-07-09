import re


def checker(pattern:dict, aunt:dict):
    for key in aunt:
        if int(aunt[key]) != pattern[key]:
            return False
    return True


reg_pattern = re.compile(r'[a-z]+: \d+')
dict_pattern = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}


with open("input.txt") as file:
    for l_index, line in enumerate(file.read().splitlines()):
        new_line = re.findall(reg_pattern, line)
        for index, item in enumerate(new_line):
            new_line[index] = item.split(': ')
        new_line = dict(new_line)
        if checker(dict_pattern, new_line) is True:
            print(l_index + 1)
