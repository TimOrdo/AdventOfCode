import re


template_one = re.compile('[aeiou]')
template_two = re.compile('ab|cd|pq|xy')
template_three = re.compile(r'(.)\1')
counter = 0
with open("input.txt") as file:
    for line in file.read().splitlines():
        if (len(template_one.findall(line)) >= 3
                and len(template_two.findall(line)) == 0
                and len((template_three.findall(line))) > 0):
            counter += 1
print(counter)
