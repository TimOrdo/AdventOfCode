def search_value_of(name) -> int:
    try:
        return int(name)
    except ValueError:
        pass

    if name not in results:
        helper = items[name]
        if len(helper) == 1:
            results[name] = search_value_of(helper[0])
        else:
            helper_2 = helper[-2]
            if helper_2 == 'AND':
                results[name] = search_value_of(helper[0]) & search_value_of(helper[2])
            elif helper_2 == 'OR':
                results[name] = search_value_of(helper[0]) | search_value_of(helper[2])
            elif helper_2 == 'NOT':
                results[name] = ~search_value_of(helper[1]) & 0xffff
            elif helper_2 == 'RSHIFT':
                results[name] = search_value_of(helper[0]) >> search_value_of(helper[2])
            elif helper_2 == 'LSHIFT':
                results[name] = search_value_of(helper[0]) << search_value_of(helper[2])
    return results[name]


items = dict()
results = dict()
with open("input.txt") as file:
    for line in file.read().splitlines():
        items[line.split('->')[1].strip()] = line.split('->')[0].strip().split(' ')
items['b'] = [16076]
print(search_value_of('a'))
