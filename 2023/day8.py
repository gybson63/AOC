from collections import defaultdict
from itertools import cycle
import math

def node_from_str(str):
    if str=='':
        return
    split = str.split(' = ')
    node_name = split[0]
    node_left_name, node_right_name = split[1][1:-1].split(', ')
    #d.setdefault(k, []).append(v)
    map.setdefault(node_name, {'L':node_left_name, 'R':node_right_name, 'able':1})
    map[node_name]['L'] = node_left_name
    map[node_name]['R'] = node_right_name
    map[node_name]['able'] = 1

#
# read from file
#
with open('input\input_8.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

'''
input_lines = [
"RL",
"",
"AAA = (BBB, CCC)",
"BBB = (DDD, EEE)",
"CCC = (ZZZ, GGG)",
"DDD = (DDD, DDD)",
"EEE = (EEE, EEE)",
"GGG = (GGG, GGG)",
"ZZZ = (ZZZ, ZZZ)"
]
'''
map = defaultdict(defaultdict)
instructions = input_lines[0]
nodes = input_lines[2:-1]
for node in nodes:
    node_from_str(node)

def step_from_node(n):
    step = 0
    l = len(instructions)
    cur_node = n
    while cur_node[2] != "Z":
        dir = instructions[step%l]
        step+=map[cur_node]['able']
        map[cur_node]['able'] = 0
        cur_node = map[cur_node][dir]
    return step

print(step_from_node('AAA'))

'''
input_lines = [
"LR",
"",
"11A = (11B, XXX)",
"11B = (XXX, 11Z)",
"11Z = (11B, XXX)",
"22A = (22B, XXX)",
"22B = (22C, 22C)",
"22C = (22Z, 22Z)",
"22Z = (22B, 22B)",
"XXX = (XXX, XXX)"
]
'''

map = defaultdict(defaultdict)
instructions = input_lines[0]
nodes = input_lines[2:len(input_lines)]
print(nodes[-1])
for node in nodes:
    node_from_str(node)

res = []
starts = [n for n in map.keys() if n.endswith("A")]
for current in starts:
    visited = set() #chek for the second circle
    curr = current
    for count, (instr_index, instr) in enumerate(cycle(enumerate(instructions)), start=1):
        prev, curr = curr, map[curr][instr]
        visited.add((curr, instr_index))
        if prev.endswith("Z") and (curr, instr_index) in visited:
            res.append(count - 1)
            break

print(math.lcm(*res))