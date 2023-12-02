import sys

condition = {'red': 12, 'green': 13, 'blue': 14}
#
# read from file
#
with open('input\input_2.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

def parse_line(line : str)->dict:

    res = {'id': 0, 'red': 0, 'green': 0, 'blue': 0}
    first_split = line.split(':')
    second_split = first_split[0].split()
    res['id'] = int(second_split[1])
    game_content = first_split[1]

    games = game_content.split(';')
    for game in games:
        cubes = game.split(',')
        for cube in cubes:
            kv = cube.strip().split(' ')
            amount = int(kv[0])
            key = kv[1]
            if res[key]<amount:
                res[key] = amount

    return res

result = 0
games = []

for line in input_lines:
    games.append(parse_line(line))

for game in games:
    impossible = game['red']>condition['red'] or game['green']>condition['green'] or game['blue']>condition['blue']
    if not impossible:
        result += game['id']

print("day 2, part 1:", result)        

result = 0

for game in games:
    result += game['red']*game['green']*game['blue']

print("day 2, part 2:", result)
