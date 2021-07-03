import hashlib as hb

task_input = 'ugkcyxxp'

checker = True
index = 0
answer = ['_', '_', '_', '_', '_', '_', '_', '_']
while checker is True:
    result = hb.md5((task_input + str(index))
                    .encode()).hexdigest()
    if result[0:5] == '00000':
        try:
            if answer[int(result[5])] == '_':
                answer[int(result[5])] = str(result[6])
        except (ValueError, IndexError) as e:
            index += 1
            continue
    if '_'not in answer:
        break
    index += 1

print(''.join(answer))
