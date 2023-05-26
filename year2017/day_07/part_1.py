from collections import defaultdict
import re


def req(def_dict: defaultdict, item: str, depth=0) -> (int, str):
    it = def_dict[item]
    if len(it) > 1:
        for i in it[1:]:
            return req(def_dict, i, depth=depth+1)
    return depth, item


branches = defaultdict(list)
regex = r"\w+"

with open("input.txt") as file:
    for line in file.read().splitlines():
        groups = re.findall(regex, line)
        branches[groups[0]] = groups[1:]

count = 0
answer = ''
for branch in branches:
    c, n = req(branches, branch)
    if c > count:
        count = c
        answer = branch

print(answer, count)
