from collections import Counter
import re


sum_id = 0
pattern = re.compile(r'^([a-z\-]*)-(\d+)\[(\w+)\]$')
with open("input.txt") as file:
    for line in file.read().splitlines():
        name, sector_id, checksum = re.match(pattern, line).groups()
        counter = Counter(name.replace('-', '')).most_common()
        counter = [(-count, litera) for litera, count in counter]
        reg = ''.join(i[1] for i in sorted(counter))
        if reg.startswith(checksum):
            sum_id += int(sector_id)
print(sum_id)
