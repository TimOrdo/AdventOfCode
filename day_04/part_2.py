from hashlib import md5


puzzle_input = 'yzbqklnj'
hoop_net = puzzle_input
i = 0
while True:
    hoop_net = md5((puzzle_input + str(i)).encode()).hexdigest()
    if hoop_net[:6] == '000000':
        break
    i += 1
print(i)
