from collections import defaultdict

#
# read from file
#
with open('input\input_5.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

seeds = list(map(int, input_lines[0][7:].split(' ')))

maps = defaultdict(list)

current_map = None
for i in range(2, len(input_lines)):
    line = input_lines[i]
    if len(line) == 0:
        continue
    elif line[-1]==':':
        split = line.split(' ')[0].split('-')
        map_from = split[0]
        map_to = split[2]
        map_name = split[1]
        current_map = maps[map_to]
        continue    
    values = line.split()
    current_map.append((int(values[0]), int(values[1]), int(values[2])))

def find_dest(lst, source):
    res = source
    for dest_start, source_start, len in lst:
        source_end = source_start + len - 1
        dest_end = dest_start + len - 1
        if source<source_start or source>source_end:
            continue
        diff = source - source_start
        dest = dest_start + diff
        res = dest
    
    return res

locations = []
for seed in seeds:
    soil = find_dest(maps['soil'], seed)
    fertilizer = find_dest(maps['fertilizer'], soil)
    water = find_dest(maps['water'], fertilizer)
    light = find_dest(maps['light'], water)
    temperature = find_dest(maps['temperature'], light)
    humidity = find_dest(maps['humidity'], temperature)
    location = find_dest(maps['location'], humidity)
    locations.append(location)

print("day 5, part 1", min(locations))


def find_dest_range(lst, source):
    res = []    
    for rng in source:
        for dest_start, source_start, len in lst:
            source_end = source_start + len - 1
            dest_end = dest_start + len - 1
            if rng[1]<source_start or rng[0]>source_end:
                continue
            res_start = max(rng[0], source_start)
            res_end = min(rng[1], source_end)
            diff = dest_start - source_start
            res.append((res_start + diff, res_end + diff))
            if rng[0]<res_start-1:
                source.append((rng[0], res_start-1))
            if rng[1]-1>res_end:
                source.append((res_end+1, rng[1]))
            break
        else:
            res.append((rng[0], rng[1]))

    return res

locations = []
seeds_list = []
for i in range(0,len(seeds),2):
    seeds_list.append((seeds[i], seeds[i]+seeds[i+1]-1))

soil = find_dest_range(maps['soil'], seeds_list)
fertilizer = find_dest_range(maps['fertilizer'], soil)
water = find_dest_range(maps['water'], fertilizer)
light = find_dest_range(maps['light'], water)
temperature = find_dest_range(maps['temperature'], light)
humidity = find_dest_range(maps['humidity'], temperature)
location = find_dest_range(maps['location'], humidity)
locations.append(min(location))

print("day 5, part 2", min(min(locations)))