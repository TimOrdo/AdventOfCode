import json


def sum_finder(json_data):
    if type(json_data) is int:
        return json_data
    elif type(json_data) is list:
        return sum(map(sum_finder, json_data))
    elif type(json_data) is dict:
        if 'red' in json_data.values():
            return 0
        else:
            return sum(map(sum_finder, json_data.values()))
    else:
        return 0


with open('input.txt') as file:
    data = json.loads(file.read())
    print(sum_finder(data))