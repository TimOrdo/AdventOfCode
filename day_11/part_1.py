import re
from string import ascii_lowercase as a_l


def rec_count(in_string: str):
    if in_string[-1] == 'z':
        return rec_count(in_string[:-1]) + 'a'
    else:
        return in_string[:-1] + a_l[a_l.index(in_string[-1]) + 1]


input_string = 'hepxcrrq'

pattern_1 = list()
for index in range(len(a_l) - 2):
    pattern_1.append(a_l[index:index + 3])

pattern_2 = re.compile(r'(.)\1')
pattern_3 = re.compile(r'i|l|o')


while True:
    checker_01 = False
    checker_02 = False
    checker_03 = True
    for item in pattern_1:
        if item in input_string:
            checker_01 = True
            break

    if len(re.findall(pattern_2, input_string)) == 2:
        checker_02 = True

    if re.findall(pattern_3, input_string):
        checker_03 = False

    if checker_01 is True and checker_02 is True and checker_03 is True:
        print(input_string)
        break
    else:
        input_string = rec_count(input_string)
