from collections import Counter, deque
import re
import string


def decode(in_string: str, in_sect_id):
    alphabet = string.ascii_lowercase
    new_alphabet = deque(alphabet)
    new_alphabet.rotate(-in_sect_id % len(alphabet))
    return in_string.translate(str.maketrans(
        alphabet,
        ''.join(i for i in new_alphabet)
    ))


sum_id = 0
pattern = re.compile(r'^([a-z\-]*)-(\d+)\[(\w+)\]$')
with open("input.txt") as file:
    for line in file.read().splitlines():
        name, sector_id, checksum = re.match(pattern, line).groups()
        counter = Counter(name.replace('-', '')).most_common()
        counter = [(-count, litera) for litera, count in counter]
        reg = ''.join(i[1] for i in sorted(counter))
        if reg.startswith(checksum):
            decoded = decode(name, int(sector_id))
            if 'north' in decoded:
                print(sector_id)
