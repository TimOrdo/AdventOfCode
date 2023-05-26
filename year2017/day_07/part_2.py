from collections import defaultdict
import re


def req(def_dict: defaultdict, item: list, depth=0, depth_list=[]) -> (int, list):
    depth_list.append(item)
    it = def_dict[item]
    if len(it) > 1:
        for i in it[1:]:
            return req(def_dict, i, depth=depth+1)
    return depth, item, depth_list


branches = defaultdict(list)
regex = r"\w+"

with open("input.txt") as file:
    for line in file.read().splitlines():
        groups = re.findall(regex, line)
        branches[groups[0]] = groups[1:]

count = 0
answer = ''
stack = list()

for branch in branches:
    c, n, s = req(branches, branch)
    if c > count:
        count = c
        stack = s.copy()
        answer = branch

# stack = set(stack)

for i in stack:
    test = branches[i]
    summa = int(branches[i][0])
    if len(branches[i][1:]) > 1:
        for b in branches[i][1:]:
            summa += int(branches[b][0])
    print(summa)

