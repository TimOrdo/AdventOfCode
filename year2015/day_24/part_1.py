import itertools
from typing import Iterable


def multi(lst: Iterable):
    answer = 1
    for item in lst:
        answer *= item
    return answer


answer_list = list()
gifts_weight = list()
with open("input.txt") as file:
    for line in file.read().splitlines():
        gifts_weight.append(int(line))

group_weight = sum(gifts_weight) // 3

for n in range(len(gifts_weight) // 3):
    for package in itertools.combinations(gifts_weight, n):
        if sum(package) == group_weight:
            answer_list.append(multi(package))

print(min(answer_list))
