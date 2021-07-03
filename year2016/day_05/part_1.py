import hashlib as hb

task_input = 'ugkcyxxp'

checker = True
index = 0
answer = ''
while checker is True:
    result = hb.md5((task_input + str(index))
                    .encode()).hexdigest()
    if result[0:5] == '00000':
        answer += result[5]
        if len(answer) > 7:
            break
    index += 1

print(answer)
