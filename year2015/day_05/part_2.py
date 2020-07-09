import re


template_one = re.compile(r'(.).\1')
template_two = re.compile(r'(..).*\1')
counter = 0
with open("input.txt") as file:
    for line in file.read().splitlines():
        if (len(template_one.findall(line)) >= 1
                and len(template_two.findall(line)) >= 1):
            counter += 1
print(counter)
